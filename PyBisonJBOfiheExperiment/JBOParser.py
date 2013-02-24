#!/usr/bin/env python

import bison

class Parser(bison.BisonParser):

    tokens = ['GARBAGE','A','BAhE','BAI','BE','BEhO','BEI','BIhE','BIhI','BO','BOI','BRIVLA','BU','BY','CAhA','CAI','CEhE','CEI','CMENE','CO','COI','CU','CUhE','DAhO','DOhU','DOI','FA','FAhA','FAhO','FEhE','FEhU','FIhO','FOI','FUhA','FUhE','FUhO','GA','GAhO','GEhU','GI','GIhA','GOhA','GOI','GUhA','I','JA','JAI','JOhI','JOI','KE','KEhE','KEI','KI','KOhA','KUhE','KUhO','KU','LA','LAhE','LAU','LE','LEhU','LI','LIhU','LOhO','LOhU','LU','LUhU','MAhO','MAI','ME','MEhU','MOhE','MOhI','MOI','NA','NAhE','NAhU','NAI','NIhE','NIhO','NOI','NU','NUhA','NUhI','NUhU','PA','PEhA','PEhE','PEhO','POhA','PU','RAhO','ROI','SA','SE','SEhU','SEI','SI','SOI','SU','TAhE','TEhU','TEI','TO','TOI','TUhE','TUhU','UI','VA','VAU','VEhA','VEhO','VEI','VIhA','VUhO','VUhU','XI','Y','ZAhO','ZEhA','ZEI','ZI','ZIhE','ZO','ZOhU','ZOI','PRIVATE_START_EK','PRIVATE_START_GIHEK','PRIVATE_START_GUHEK','PRIVATE_START_JEK','PRIVATE_END_JEK','PRIVATE_START_JOIK','PRIVATE_END_JOIK','PRIVATE_START_GEK','PRIVATE_START_BAI','PRIVATE_EK_KE','PRIVATE_EK_BO','PRIVATE_JEK_KE','PRIVATE_JEK_BO','PRIVATE_JOIK_KE','PRIVATE_JOIK_BO','PRIVATE_I_JEKJOIK','PRIVATE_I_BO','PRIVATE_GIHEK_KE','PRIVATE_GIHEK_BO','PRIVATE_NAhE_BO','PRIVATE_NAhE_time','PRIVATE_NAhE_space','PRIVATE_NAhE_CAhA','PRIVATE_NA_KU','PRIVATE_NUMBER_MAI','PRIVATE_NUMBER_MOI','PRIVATE_NUMBER_ROI','PRIVATE_START_TENSE','PRIVATE_END_TENSE','PRIVATE_EOF_MARK','IMPOSSIBLE_TOKEN']

    precedences=[]

    lexscript = "\n".join(open("cm_scan.l", "r").readlines())


p = Parser()
