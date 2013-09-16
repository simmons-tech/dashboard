### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

all: core-dashboard clock-widget dining-widget events-widget laundry-widget news-widget nextbus-widget package_list-widget weather-widget

core-dashboard:
	coffee -c dashboard/static/js/*.coffee
	lessc -x dashboard/static/css/style.less > dashboard/static/css/style.css
	lessc -x dashboard/static/css/sevenk.less > dashboard/static/css/sevenk.css
	lessc -x dashboard/static/css/lightweight.less > dashboard/static/css/lightweight.css

clock-widget:
	coffee -c clock/static/js/*.coffee

dining-widget:
	coffee -c dining/static/js/*.coffee

events-widget:
	coffee -c events/static/js/*.coffee

laundry-widget:
	coffee -c laundry/static/js/*.coffee

news-widget:
	coffee -c news/static/js/*.coffee

nextbus-widget:
	coffee -c nextbus/static/js/*.coffee

package_list-widget:
	coffee -c package_list/static/js/*.coffee

weather-widget:
	coffee -c weather/static/js/*.coffee
