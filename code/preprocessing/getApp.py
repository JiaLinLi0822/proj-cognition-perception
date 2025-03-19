import os
import glob
import pandas as pd
import numpy as np
import json
import re

def getApp(code5File, saveDatafilePath, rawDatafilePath):

    f = open(code5File)
    dat=json.load(f)
    
    ps = dat['meta_data']['user_name']
    if ps == '1cog2' or ps == '2cog2':
        ps = ''.join(filter(str.isdigit, ps))
        ps = ps[0]

    for m in dat['data']:
        gameDict = m
        # print(m)
        if 'game_mode' not in gameDict:
            return 
        else:
            if gameDict['game_mode']=='CorsiSimple' or gameDict['game_mode']=='a_CorsiComplex': #splitting by task
                c_forward = gameDict['longest_forward_sequence_length']
                # print(c_forward[-1])
                #print(len(c_forward))

                print('get Corsi data from participant ' + ps)
                CorsiInd = [c_forward]
                
            if gameDict['game_mode']=='LetterNumberSpan' or gameDict['game_mode']=='a_LetterNumberSpan':
                lns_length = gameDict['calculated_target_length']
                lns_hit = gameDict['hit']
                lns_miss = gameDict['miss']
                
                #calculate hit rate (proportion of hits/total trials)
                lns_hitRate = gameDict['hit']/(gameDict['hit']+gameDict['miss'])
                #print(lns_hitRate)
                
                print('get LetterNumberSpan data from participant ' + ps)
                LNSInd = [lns_length, lns_hit, lns_miss, lns_hitRate]
            
            if gameDict['game_mode']== 'D2' or gameDict['game_mode']== 'a_D2':
                d2_hit = gameDict['hits']
                d2_miss = gameDict['misses']
                d2_FA = gameDict['false_alarms']
                d2_CR = gameDict['correct_rejections']
                
                #calculate hit rate
                hiR = gameDict['hits']/(gameDict['hits']+gameDict['misses'])
                d2_hitRate = gameDict['hits']/(gameDict['hits']+gameDict['misses'])
                #print(d2_hitRate)
                
                #calculate FA rate 
                faR = gameDict['false_alarms']/(gameDict['false_alarms']+gameDict['correct_rejections'])
                d2_faRate = gameDict['false_alarms']/(gameDict['false_alarms']+gameDict['correct_rejections'])
                #print(d2_faRate)
                
                #adj hit rate (hit Rate - FA rate)
                d2_adjHitR = hiR-faR
                #print(d2_adjHitR)
                print('get D2 data from participant ' + ps)

                D2Ind = [d2_hit, d2_miss, d2_FA, d2_CR, d2_hitRate, d2_faRate, d2_adjHitR]

    return [int(ps)], CorsiInd, LNSInd, D2Ind