import os
import json
from pathlib import Path
from jproperties import Properties


class DirUtils:
    def get_work_dir(self):
        return os.getcwd()

    def get_src_dir(self):
        return os.path.join(self.get_work_dir(), 'src')

    def get_utils_dir(self):
        return os.path.join(self.get_src_dir(), 'utils')

    def get_events_dir(self):
        return os.path.join(self.get_utils_dir(), 'events')

    def get_subprocesses_dir(self):
        return os.path.join(self.get_events_dir(), 'subprocesses')

    def get_media_dir(self):
        return os.path.join(self.get_src_dir(), 'media')

    def get_mood_dir(self):
        return os.path.join(self.get_media_dir(), 'moods')

    def get_data_dir(self):
        return os.path.join(self.get_src_dir(), 'data')

    def get_cache_dir(self):
        return os.path.join(self.get_data_dir(), 'cache')

    def get_schema_dir(self):
        return os.path.join(self.get_data_dir(), 'schema')

    # use AI to figure out where a ceratin user directory is
    def find_path(self, end_dir):

        # convert end dir to lowercase and titlecase
        end_dir = end_dir.lower().title()

        home_path = Path.home()
        # filter out hidden directories

        def is_hidden(x):
            return '.' not in x

        def lowercase_all(x):
            return x.title()

        dir_list = map(lowercase_all, filter(is_hidden, os.listdir(home_path)))

        test_path = os.path.abspath(os.path.join(home_path, end_dir))
        return test_path if os.path.exists(test_path) and end_dir in dir_list else home_path

    # get typical os-agnostic userdirectories
    def get_user_pictures_dir(self):
        return self.find_path('Pictures')

    def get_user_downloads_dir(self):
        return self.find_path('Downloads')

    def get_user_documents_dir(self):
        return self.find_path('Documents')

    def get_user_music_dir(self):
        return self.find_path('Music')

    def get_user_video_dir(self):
        return self.find_path('Videos')

    def get_user_desktop_dir(self):
        return self.find_path('desktop')

    def read_json(self, dir, json_file):
        f = open(os.path.join(dir, json_file))
        data = json.load(f)
        f.close()
        return data

    def write_json(self, dir, json_file, dict_contents):
        # Serializing json
        json_object = json.dumps(dict_contents, indent=4)

        # Writing to sample.json
        with open(os.path.join(dir, json_file), "w") as outfile:
            outfile.write(json_object)
        outfile.close()

    def read_properties(self, dir, properties_file):
        configs = Properties()
        # different properties change the ways events play out, so read them in
        with open(os.path.join(dir, properties_file), 'rb') as config_file:
            configs.load(config_file)

        items_view = configs.items()

        db_configs_dict = {}

        for item in items_view:
            db_configs_dict[item[0]] = int(item[1].data)

        return db_configs_dict
