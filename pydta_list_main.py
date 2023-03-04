# -*- coding:utf-8 -*-
##############################################################
# Created Date: Friday, March 3rd 2023
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


from pyDTALite import perform_network_assignment_DTALite


if __name__ == "__main__":
    # perform network assignment using DTALite
    perform_network_assignment_DTALite(assignment_mode=2,
                                       column_gen_num=10,
                                       column_update_num=10)