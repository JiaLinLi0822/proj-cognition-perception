import os
import shutil

def classification1():

    # 原始数据文件夹路径
    source_folder = '/Users/lijialin/Downloads/Cognition Project/ExpData_011123/'

    # 目标文件夹路径，存储不同类别的文件
    target_folders = {
        'App Task': '/Users/lijialin/Downloads/Cognition Project/data/App Task',
        'Cognition Task': '/Users/lijialin/Downloads/Cognition Project/data/Cognition Task',
        'Perceptual Task': '/Users/lijialin/Downloads/Cognition Project/data/Perceptual Task',
        'Speech Task': '/Users/lijialin/Downloads/Cognition Project/data/Speech Task',
        'Trial Task': '/Users/lijialin/Downloads/Cognition Project/data/Trial Task',
        'others': '/Users/lijialin/Downloads/Cognition Project/data/others',
    }

    # 创建目标文件夹
    for folder_path in target_folders.values():
        os.makedirs(folder_path, exist_ok=True)

    # 遍历原始数据文件夹中的文件名
    for filename in os.listdir(source_folder):
        # 如果是文件夹则跳过
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue
        # 判断文件名是否以 ".json" 结尾，并且不包含 "strategy" 字符串
        if filename.endswith('.json') and 'CorsiSimpleAction' in filename:
            # Move to App Task folder
            task = 'App Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')

        elif filename.endswith('.csv') and 'Cognition2' in filename:
            # Move to Cognition Task folder
            task = 'Cognition Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        elif filename.endswith('.csv') and 'SIFI_RandomRespOrder' in filename:
            # Move to Perceptual Task folder
            task = 'Perceptual Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        elif filename.endswith('.csv') and 'SpeechDraft1Carolyn' in filename:
            # Move to Speech Task folder
            task = 'Speech Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        elif filename.endswith('.csv') and 'trailMaking' in filename:
            # Move to Trial Task folder
            task = 'Trial Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        else:
            # Move to others folder
            task = 'others'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')

def classification2():

    # 原始数据文件夹路径
    source_folder = '/Users/lijialin/Downloads/Cognition Project/ExpData_011123/TrailData/'

    # 目标文件夹路径，存储不同类别的文件
    target_folders = {
        'Trial Task': '/Users/lijialin/Downloads/Cognition Project/data/Trial Task',
        'others': '/Users/lijialin/Downloads/Cognition Project/data/others',
    }

    # 创建目标文件夹
    for folder_path in target_folders.values():
        os.makedirs(folder_path, exist_ok=True)

    # 遍历原始数据文件夹中的文件名
    for filename in os.listdir(source_folder):
        # 如果是文件夹则跳过
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue
     
        if filename.endswith('.csv') and 'trailMaking' in filename:
            # Move to Trial Task folder
            task = 'Trial Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        else:
            # Move to others folder
            task = 'others'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')

def classification3():
    # 原始数据文件夹路径
    source_folder = '/Users/lijialin/Downloads/Cognition Project/ExpData_011123/AppData_storage/'

    # 目标文件夹路径，存储不同类别的文件
    target_folders = {
        'App Task': '/Users/lijialin/Downloads/Cognition Project/data/App Task',
        'others': '/Users/lijialin/Downloads/Cognition Project/data/others',
    }

    # 创建目标文件夹
    for folder_path in target_folders.values():
        os.makedirs(folder_path, exist_ok=True)

    # 遍历原始数据文件夹中的文件名
    for filename in os.listdir(source_folder):
        # 如果是文件夹则跳过
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue

        if filename.endswith('.json') and 'SummaryLog' in filename:
            # Move to App Task folder
            task = 'App Task'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')
        
        else:
            # Move to others folder
            task = 'others'
            source_file_path = os.path.join(source_folder, filename)
            target_folder = target_folders.get(task)
            target_file_path = os.path.join(target_folder, filename)

            shutil.copyfile(source_file_path, target_file_path)
            print(f'Copied {filename} to {target_folder}')

if __name__ == '__main__':
    # classification1()
    classification2()
    classification3()

