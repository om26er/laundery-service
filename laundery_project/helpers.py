# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

#
# Simple Login
# Copyright (C) 2016 byteShaft
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import configparser
import random

import requests

CONFIG_FILE = os.path.expanduser('~/sample_config.ini')
CONFIG_SECTION_DEFAULT = 'defaults'
CONFIG_SECTION_SMS_OTP = 'sms_otp'
CONFIG_SECTION_EMAIL_CREDENTIALS = 'email_credentials'
CONFIG_SECTION_DATABASE_CREDENTIALS = 'database_credentials'

URL_SMS_OTP = 'http://smpp2.onlysms.ae/api/api_http.php?username={username}&' \
              'password={password}&senderid={sender}&to={to}&' \
              'text={message}&type=text'


class ConfigHelpers:
    def __init__(self, config_file=CONFIG_FILE):
        if not os.path.isfile(config_file):
            raise RuntimeError('Config file does not exist.')
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def read_config_parameter(self, config_section, config_key):
        try:
            return self.config.get(config_section, config_key)
        except configparser.NoOptionError or configparser.NoSectionError:
            return None

    def get_email_credential_by_key(self, key):
        return self.read_config_parameter(
            CONFIG_SECTION_EMAIL_CREDENTIALS,
            key
        )

    def get_database_credential_by_key(self, key):
        return self.read_config_parameter(
            CONFIG_SECTION_DATABASE_CREDENTIALS,
            key
        )

    def get_debug_setting(self):
        value = self.read_config_parameter(CONFIG_SECTION_DEFAULT, 'debug')
        return value == 'True'

    def get_server_ip(self):
        return self.read_config_parameter(CONFIG_SECTION_DEFAULT, 'server_ip')


def generate_and_send_sms_otp(mobile_number):
    ch = ConfigHelpers()
    code = random.randint(10000, 99999)
    url = URL_SMS_OTP.format(
        username=ch.read_config_parameter(CONFIG_SECTION_SMS_OTP, 'username'),
        password=ch.read_config_parameter(CONFIG_SECTION_SMS_OTP, 'password'),
        sender=ch.read_config_parameter(CONFIG_SECTION_SMS_OTP, 'sender'),
        to=mobile_number,
        message=code,
    )
    print(url)
    requests.post(url)
    return code
