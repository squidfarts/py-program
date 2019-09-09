#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: setup.py                                                                  #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michaelbrockus@squidfarts.com>                                 #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
import setuptools, setup



setup(
    name='py-program',
    version='0.1.0',
    description='Python program',
    author='Michael Brockus',
    author_email='michaelbrockus@squidfarts.com',
    license='Apache-2.0',
    include_package_data=True,
    packages=['src.main', 'src.main.module']
)