"""
Name: Dandere2X Frame
Author: CardinalPanda
Date Created: 5-4-2019
Last Modified: 5-4-2019

Description:

Have all the variables used in Dandere2x stored in here
and have this class be passed to scripts
rather than passing like 8-9 variables
"""

import configparser
import logging
import os
from wrappers.ff_wrappers.videosettings import VideoSettings

# init is pretty messy at the moment. I'll look into
# cleaning this up in the future ;-;
class Context:

    def __init__(self, config_file: str):
        config = configparser.ConfigParser()
        config.read(config_file)

        self.this_folder = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

        # directories
        self.waifu2x_caffe_cui_dir = config.get('dandere2x', 'waifu2x_caffe_cui_dir')
        self.model_dir = config.get('dandere2x', 'model_dir')

        self.workspace = config.get('dandere2x', 'workspace')
        self.file_dir = config.get('dandere2x', 'file_dir')

        self.dandere2x_cpp_dir = config.get('dandere2x', 'dandere2x_cpp_dir')

        self.ffmpeg_dir = config.get('dandere2x', 'ffmpeg_dir')
        self.ffprobe_dir = config.get('dandere2x', 'ffprobe_dir')

        self.waifu2x_type = config.get('dandere2x', 'waifu2x_type')

        self.waifu2x_conv_dir = config.get('dandere2x', 'waifu2x_conv_dir')
        self.waifu2x_conv_dir_dir = config.get('dandere2x', 'waifu2x_conv_dir_dir')

        self.waifu2x_vulkan_dir = config.get('dandere2x', 'waifu2x_vulkan_dir')
        self.waifu2x_vulkan_dir_dir = config.get('dandere2x', 'waifu2x_vulkan_dir_dir')

        if '[this]' in self.waifu2x_conv_dir:
            self.waifu2x_conv_dir = self.waifu2x_conv_dir.replace('[this]', self.this_folder)

        if '[this]' in self.waifu2x_conv_dir_dir:
            self.waifu2x_conv_dir_dir = self.waifu2x_conv_dir_dir.replace('[this]', self.this_folder)

        if '[this]' in self.waifu2x_vulkan_dir:
            self.waifu2x_vulkan_dir = self.waifu2x_vulkan_dir.replace('[this]', self.this_folder)

        if '[this]' in self.waifu2x_vulkan_dir_dir:
            self.waifu2x_vulkan_dir_dir = self.waifu2x_vulkan_dir_dir.replace('[this]', self.this_folder)

        # parse [this] for release versions (removing this feature in the future, just for early testing.

        if '[this]' in self.waifu2x_caffe_cui_dir:
            self.waifu2x_caffe_cui_dir = self.waifu2x_caffe_cui_dir.replace('[this]', self.this_folder)

        if '[this]' in self.workspace:
            self.workspace = self.workspace.replace('[this]', self.this_folder)

        if '[this]' in self.dandere2x_cpp_dir:
            self.dandere2x_cpp_dir = self.dandere2x_cpp_dir.replace('[this]', self.this_folder)

        if '[this]' in self.ffmpeg_dir:
            self.ffmpeg_dir = self.ffmpeg_dir.replace('[this]', self.this_folder)

        if '[this]' in self.ffprobe_dir:
            self.ffprobe_dir = self.ffprobe_dir.replace('[this]', self.this_folder)

        if '[this]' in self.file_dir:
            self.file_dir = self.file_dir.replace('[this]', self.this_folder)

        if '[this]' in self.model_dir:
            self.model_dir = self.model_dir.replace('[this]', self.this_folder)

        self.video_settings = VideoSettings(self.ffprobe_dir, self.file_dir)

        self.frame_rate = self.video_settings.frame_rate
        self.width = self.video_settings.width
        self.height = self.video_settings.height


        # linux
        self.dandere_dir = config.get('dandere2x', 'dandere_dir')
        self.audio_layer = config.get('dandere2x', 'audio_layer')

        # D2x Settings

        self.block_size = int(config.get('dandere2x', 'block_size'))
        self.step_size = config.get('dandere2x', 'step_size')
        self.bleed = int(config.get('dandere2x', 'bleed'))
        self.quality_low = int(config.get('dandere2x', 'quality_low'))
        self.realtime_encoding = int(config.get('dandere2x', 'realtime_encoding'))
        self.realtime_encoding_delete_files = int(config.get('dandere2x', 'realtime_encoding_delete_files'))

        # todo idunno if theres a better way to figure out how many frames will be used.
        self.frame_count = 0

        # waifu2x settings
        self.noise_level = config.get('dandere2x', 'noise_level')
        self.scale_factor = config.get('dandere2x', 'scale_factor')
        self.extension_type = config.get('dandere2x', 'extension_type')
        self.audio_type = config.get('dandere2x', 'audio_type')


        # setup directories
        self.input_frames_dir = self.workspace + "inputs" + os.path.sep
        self.differences_dir = self.workspace + "differences" + os.path.sep
        self.upscaled_dir = self.workspace + "upscaled" + os.path.sep
        self.correction_data_dir = self.workspace + "correction_data" + os.path.sep
        self.merged_dir = self.workspace + "merged" + os.path.sep
        self.inversion_data_dir = self.workspace + "inversion_data" + os.path.sep
        self.pframe_data_dir = self.workspace + "pframe_data" + os.path.sep
        self.fade_data_dir = self.workspace + "fade_data" + os.path.sep
        self.debug_dir = self.workspace + "debug" + os.path.sep
        self.log_dir = self.workspace + "logs" + os.path.sep
        self.compressed_dir = self.workspace + "compressed" + os.path.sep
        self.encoded_dir = self.workspace + "encoded" + os.path.sep

        # Developer Settings #
        self.debug = int(config.get('dandere2x', 'debug'))

        # Waifu2x-wrappers Commands
        self.waifu2x_vulkan_upscale_frame = config.get('dandere2x', 'waifu2x_vulkan_upscale_frame')
        self.waifu2x_caffe_upscale_frame = config.get('dandere2x', 'waifu2x_caffe_upscale_frame')

        # FFMPEG Options #

        self.migrate_tracks_command = config.get('dandere2x', 'migrate_tracks_command')
        self.extract_audio_command = config.get('dandere2x', 'extract_audio_command')
        self.extract_frames_command = config.get('dandere2x', 'extract_frames_command')
        self.video_from_frames_command = config.get('dandere2x', 'video_from_frames_command')
        self.merge_video_command = config.get('dandere2x', 'merge_video_command')

        logging.basicConfig(filename='dandere2x.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)



    def update_frame_count(self):
        self.frame_count = len([name for name in os.listdir(self.input_frames_dir)
                                if os.path.isfile(os.path.join(self.input_frames_dir, name))])
