#!/usr/bin/env python

import bison

class Parser(bison.BisonParser):

    tokens = ['GARBAGE', 'A', 'BAhE', 'BAI', 'BE', 'BEhO', 'BEI', 'BIhE', 'BIhI', 'BO', 'BOI', 'BRIVLA', 'BU', 'BY', 'CAhA', 'CAI', 'CEhE', 'CEI', 'CMENE', 'CO', 'COI', 'CU', 'CUhE', 'DAhO', 'DOhU', 'DOI', 'FA', 'FAhA', 'FAhO', 'FEhE', 'FEhU', 'FIhO', 'FOI', 'FUhA', 'FUhE', 'FUhO', 'GA', 'GAhO', 'GEhU', 'GI', 'GIhA', 'GOhA', 'GOI', 'GUhA', 'I', 'JA', 'JAI', 'JOhI', 'JOI', 'KE', 'KEhE', 'KEI', 'KI', 'KOhA', 'KUhE', 'KUhO', 'KU', 'LA', 'LAhE', 'LAU', 'LE', 'LEhU', 'LI', 'LIhU', 'LOhO', 'LOhU', 'LU', 'LUhU', 'MAhO', 'MAI', 'ME', 'MEhU', 'MOhE', 'MOhI', 'MOI', 'NA', 'NAhE', 'NAhU', 'NAI', 'NIhE', 'NIhO', 'NOI', 'NU', 'NUhA', 'NUhI', 'NUhU', 'PA', 'PEhA', 'PEhE', 'PEhO', 'POhA', 'PU', 'RAhO', 'ROI', 'SA', 'SE', 'SEhU', 'SEI', 'SI', 'SOI', 'SU', 'TAhE', 'TEhU', 'TEI', 'TO', 'TOI', 'TUhE', 'TUhU', 'UI', 'VA', 'VAU', 'VEhA', 'VEhO', 'VEI', 'VIhA', 'VUhO', 'VUhU', 'XI', 'Y', 'ZAhO', 'ZEhA', 'ZEI', 'ZI', 'ZIhE', 'ZO', 'ZOhU', 'ZOI', 'PRIVATE_START_EK', 'PRIVATE_START_GIHEK', 'PRIVATE_START_GUHEK', 'PRIVATE_START_JEK', 'PRIVATE_END_JEK', 'PRIVATE_START_JOIK', 'PRIVATE_END_JOIK', 'PRIVATE_START_GEK', 'PRIVATE_START_BAI', 'PRIVATE_EK_KE', 'PRIVATE_EK_BO', 'PRIVATE_JEK_KE', 'PRIVATE_JEK_BO', 'PRIVATE_JOIK_KE', 'PRIVATE_JOIK_BO', 'PRIVATE_I_JEKJOIK', 'PRIVATE_I_BO', 'PRIVATE_GIHEK_KE', 'PRIVATE_GIHEK_BO', 'PRIVATE_NAhE_BO', 'PRIVATE_NAhE_time', 'PRIVATE_NAhE_space', 'PRIVATE_NAhE_CAhA', 'PRIVATE_NA_KU', 'PRIVATE_NUMBER_MAI', 'PRIVATE_NUMBER_MOI', 'PRIVATE_NUMBER_ROI', 'PRIVATE_START_TENSE', 'PRIVATE_END_TENSE', 'PRIVATE_EOF_MARK', 'IMPOSSIBLE_TOKEN']
    precedences=[]

    lexscript = "\n".join(open("cm_scan.l", "r").readlines())

    start = "input"


    def on_all(self, target, option, names, values):
        """all : chunks
all : chunks
{ top = $1; }
"""
        print "on_all: got %s %s %s %s" % (target, option, names, values)
        return

    def on_chunks(self, target, option, names, values):
        """chunks : text PRIVATE_EOF_MARK
chunks : text PRIVATE_EOF_MARK
{$$ = new_node_1(CHUNKS,$1);}
       | text error
{ $$ = $1; yyclearin; }
       | chunks text PRIVATE_EOF_MARK
{$$ = new_node_2(CHUNKS,$1,$2);}
       | chunks text error
{ fprintf(stderr, "Syntax error following text ending at line %d column %d\n",
          @2.last_line, @2.last_column);
  yyclearin;
  $$ = new_node_2(CHUNKS, $1, $2); }
"""
        print "on_chunks: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text(self, target, option, names, values):
        """text : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq text_1
text : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq text_1
{$$ = new_node_6(TEXT,$1,$2,$3,$4,$5,$6);}
     | NAI_seq CMENE_seq free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_6(TEXT,$1,$2,$3,$4,$5,$6);}
     | NAI_seq CMENE_seq free_seq joik_opt_ke          text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq free_seq jek_opt_ke           text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq free_seq                      text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq          joik_opt_ke free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq          jek_opt_ke  free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq          joik_opt_ke          text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq          jek_opt_ke           text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq                               text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     | NAI_seq indicators free_seq joik_opt_ke free_seq text_1
{$$ = new_node_6(TEXT,$1,$2,$3,$4,$5,$6);}
     | NAI_seq indicators free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_6(TEXT,$1,$2,$3,$4,$5,$6);}
     | NAI_seq indicators free_seq joik_opt_ke          text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq indicators free_seq jek_opt_ke           text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq indicators free_seq                      text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq indicators          joik_opt_ke free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq indicators          jek_opt_ke  free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq indicators          joik_opt_ke          text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq indicators          jek_opt_ke           text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq indicators                               text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     | NAI_seq            free_seq joik_opt_ke free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq            free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     | NAI_seq            free_seq joik_opt_ke          text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq            free_seq jek_opt_ke           text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq            free_seq                      text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     | NAI_seq                     joik_opt_ke free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq                     jek_opt_ke  free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     | NAI_seq                     joik_opt_ke          text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     | NAI_seq                     jek_opt_ke           text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     | NAI_seq                                          text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |         CMENE_seq free_seq joik_opt_ke free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     |         CMENE_seq free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     |         CMENE_seq free_seq joik_opt_ke          text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         CMENE_seq free_seq jek_opt_ke           text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         CMENE_seq free_seq                      text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         CMENE_seq          joik_opt_ke free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         CMENE_seq          jek_opt_ke  free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         CMENE_seq          joik_opt_ke          text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         CMENE_seq          jek_opt_ke           text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         CMENE_seq                               text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |         indicators free_seq joik_opt_ke free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     |         indicators free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_5(TEXT,$1,$2,$3,$4,$5);}
     |         indicators free_seq joik_opt_ke          text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         indicators free_seq jek_opt_ke           text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         indicators free_seq                      text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         indicators          joik_opt_ke free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         indicators          jek_opt_ke  free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |         indicators          joik_opt_ke          text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         indicators          jek_opt_ke           text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |         indicators                               text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |                    free_seq joik_opt_ke free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |                    free_seq jek_opt_ke  free_seq text_1
{$$ = new_node_4(TEXT,$1,$2,$3,$4);}
     |                    free_seq joik_opt_ke          text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |                    free_seq jek_opt_ke           text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |                    free_seq                      text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |                             joik_opt_ke free_seq text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |                             jek_opt_ke  free_seq text_1
{$$ = new_node_3(TEXT,$1,$2,$3);}
     |                             joik_opt_ke          text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |                             jek_opt_ke           text_1
{$$ = new_node_2(TEXT,$1,$2);}
     |                                                  text_1
{$$ = new_node_1(TEXT,$1);}
"""
        print "on_text: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text_no_text_1(self, target, option, names, values):
        """text_no_text_1 : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq
text_no_text_1 : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq
{$$ = new_node_5(TEXT_NO_TEXT_1,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq free_seq jek_opt_ke  free_seq
{$$ = new_node_5(TEXT_NO_TEXT_1,$1,$2,$3,$4,$5);}
     | NAI_seq CMENE_seq free_seq joik_opt_ke
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq free_seq jek_opt_ke
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq CMENE_seq          joik_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq          jek_opt_ke  free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq CMENE_seq          joik_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq CMENE_seq          jek_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq CMENE_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     | NAI_seq indicators free_seq joik_opt_ke free_seq
{$$ = new_node_5(TEXT_NO_TEXT_1,$1,$2,$3,$4,$5);}
     | NAI_seq indicators free_seq jek_opt_ke free_seq
{$$ = new_node_5(TEXT_NO_TEXT_1,$1,$2,$3,$4,$5);}
     | NAI_seq indicators free_seq joik_opt_ke
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq indicators free_seq jek_opt_ke
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq indicators free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq indicators          joik_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq indicators          jek_opt_ke  free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq indicators          joik_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq indicators          jek_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq indicators
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     | NAI_seq            free_seq joik_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq            free_seq jek_opt_ke  free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     | NAI_seq            free_seq joik_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq            free_seq jek_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq            free_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     | NAI_seq                     joik_opt_ke free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq                     jek_opt_ke  free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     | NAI_seq                     joik_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     | NAI_seq                     jek_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     | NAI_seq
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
     |         CMENE_seq free_seq joik_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     |         CMENE_seq free_seq jek_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     |         CMENE_seq free_seq joik_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         CMENE_seq free_seq jek_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         CMENE_seq free_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         CMENE_seq          joik_opt_ke free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         CMENE_seq          jek_opt_ke  free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         CMENE_seq          joik_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         CMENE_seq          jek_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         CMENE_seq
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
     |         indicators free_seq joik_opt_ke free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     |         indicators free_seq jek_opt_ke  free_seq
{$$ = new_node_4(TEXT_NO_TEXT_1,$1,$2,$3,$4);}
     |         indicators free_seq joik_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         indicators free_seq jek_opt_ke
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         indicators free_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         indicators          joik_opt_ke free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         indicators          jek_opt_ke  free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |         indicators          joik_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         indicators          jek_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |         indicators
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
     |                    free_seq joik_opt_ke free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |                    free_seq jek_opt_ke  free_seq
{$$ = new_node_3(TEXT_NO_TEXT_1,$1,$2,$3);}
     |                    free_seq joik_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |                    free_seq jek_opt_ke
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |                    free_seq
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
     |                             joik_opt_ke free_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |                             jek_opt_ke  free_seq
{$$ = new_node_2(TEXT_NO_TEXT_1,$1,$2);}
     |                             joik_opt_ke
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
     |                             jek_opt_ke
{$$ = new_node_1(TEXT_NO_TEXT_1,$1);}
"""
        print "on_text_no_text_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text_1(self, target, option, names, values):
        """text_1 : text_1A paragraphs
text_1 : text_1A paragraphs
{$$ = new_node_2(TEXT_1,$1,$2);}
       | text_1A
{$$ = new_node_1(TEXT_1,$1);}
       |         paragraphs
{$$ = new_node_1(TEXT_1,$1);}
       | 
{$$ = new_node_0(TEXT_1);}
"""
        print "on_text_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text_1A(self, target, option, names, values):
        """text_1A : text_1B
text_1A : text_1B
{$$ = new_node_1(TEXT_1A,$1);}
        | NIhO_seq_free_seq
{$$ = new_node_1(TEXT_1A,$1);}
"""
        print "on_text_1A: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text_1B(self, target, option, names, values):
        """text_1B : text_1C
text_1B : text_1C
{$$ = new_node_1(TEXT_1B,$1);}
        | text_1B text_1C
{$$ = new_node_2(TEXT_1B,$1,$2);}
"""
        print "on_text_1B: got %s %s %s %s" % (target, option, names, values)
        return

    def on_text_1C(self, target, option, names, values):
        """text_1C :         PRIVATE_I_BO I joik stag BO free_seq
text_1C :         PRIVATE_I_BO I joik stag BO free_seq
{$$ = new_node_5(TEXT_1C,$2,$3,$4,$5,$6);}
        |         PRIVATE_I_BO I jek  stag BO free_seq
{$$ = new_node_5(TEXT_1C,$2,$3,$4,$5,$6);}
        |         PRIVATE_I_BO I      stag BO free_seq
{$$ = new_node_4(TEXT_1C,$2,$3,$4,$5);}
        |         PRIVATE_I_BO I joik stag BO
{$$ = new_node_4(TEXT_1C,$2,$3,$4,$5);}
        |         PRIVATE_I_BO I jek  stag BO
{$$ = new_node_4(TEXT_1C,$2,$3,$4,$5);}
        |         PRIVATE_I_BO I      stag BO
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         PRIVATE_I_BO I joik      BO free_seq
{$$ = new_node_4(TEXT_1C,$2,$3,$4,$5);}
        |         PRIVATE_I_BO I jek       BO free_seq
{$$ = new_node_4(TEXT_1C,$2,$3,$4,$5);}
        |         PRIVATE_I_BO I           BO free_seq
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         PRIVATE_I_BO I joik      BO
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         PRIVATE_I_BO I jek       BO
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         PRIVATE_I_BO I           BO
{$$ = new_node_2(TEXT_1C,$2,$3);}
        |         PRIVATE_I_JEKJOIK I joik_opt_ke         free_seq
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         PRIVATE_I_JEKJOIK I jek_opt_ke          free_seq
{$$ = new_node_3(TEXT_1C,$2,$3,$4);}
        |         I              free_seq
{$$ = new_node_2(TEXT_1C,$1,$2);}
        |         PRIVATE_I_JEKJOIK I joik_opt_ke
{$$ = new_node_2(TEXT_1C,$2,$3);}
        |         PRIVATE_I_JEKJOIK I jek_opt_ke
{$$ = new_node_2(TEXT_1C,$2,$3);}
        |         I    
{$$ = new_node_1(TEXT_1C,$1);}
"""
        print "on_text_1C: got %s %s %s %s" % (target, option, names, values)
        return

    def on_paragraphs(self, target, option, names, values):
        """paragraphs :                              paragraph
paragraphs :                              paragraph
{$$ = new_node_1(PARAGRAPHS,$1);}
           | paragraphs NIhO_seq_free_seq paragraph
{$$ = new_node_3(PARAGRAPHS,$1,$2,$3);}
"""
        print "on_paragraphs: got %s %s %s %s" % (target, option, names, values)
        return

    def on_paragraph(self, target, option, names, values):
        """paragraph : statement
paragraph : statement
{$$ = new_node_1(PARAGRAPH,$1);}
          | fragment
{$$ = new_node_1(PARAGRAPH,$1);}
          | paragraph i_opt_free_seq statement
{$$ = new_node_3(PARAGRAPH,$1,$2,$3);}
          | paragraph i_opt_free_seq fragment
{$$ = new_node_3(PARAGRAPH,$1,$2,$3);}
          | paragraph i_opt_free_seq
{$$ = new_node_2(PARAGRAPH,$1,$2);}
"""
        print "on_paragraph: got %s %s %s %s" % (target, option, names, values)
        return

    def on_i_opt_free_seq(self, target, option, names, values):
        """i_opt_free_seq : I
i_opt_free_seq : I
{$$ = new_node_1(I_OPT_FREE_SEQ,$1);}
               | I free_seq
{$$ = new_node_2(I_OPT_FREE_SEQ,$1,$2);}
"""
        print "on_i_opt_free_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_statement(self, target, option, names, values):
        """statement : inner_statement
statement : inner_statement
{$$ = new_node_1(STATEMENT,$1);}
"""
        print "on_statement: got %s %s %s %s" % (target, option, names, values)
        return

    def on_inner_statement(self, target, option, names, values):
        """inner_statement : statement_1
inner_statement : statement_1
{$$ = new_node_1(INNER_STATEMENT,$1);}
                | prenex inner_statement
{$$ = new_node_2(INNER_STATEMENT,$1,$2);}
"""
        print "on_inner_statement: got %s %s %s %s" % (target, option, names, values)
        return

    def on_statement_1(self, target, option, names, values):
        """statement_1 : statement_2
statement_1 : statement_2
{$$ = new_node_1(STATEMENT_1,$1);}
            | statement_1 i_joik_jek statement_2
{$$ = new_node_3(STATEMENT_1,$1,$2,$3);}
            | statement_1 i_joik_jek
{$$ = new_node_2(STATEMENT_1,$1,$2);}
"""
        print "on_statement_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_i_joik_jek(self, target, option, names, values):
        """i_joik_jek : PRIVATE_I_JEKJOIK I joik_opt_ke free_seq
i_joik_jek : PRIVATE_I_JEKJOIK I joik_opt_ke free_seq
{$$ = new_node_3(I_JOIK_JEK,$2,$3,$4);}
           | PRIVATE_I_JEKJOIK I joik_opt_ke
{$$ = new_node_2(I_JOIK_JEK,$2,$3);}
           | PRIVATE_I_JEKJOIK I jek_opt_ke free_seq
{$$ = new_node_3(I_JOIK_JEK,$2,$3,$4);}
           | PRIVATE_I_JEKJOIK I jek_opt_ke
{$$ = new_node_2(I_JOIK_JEK,$2,$3);}
"""
        print "on_i_joik_jek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_statement_2(self, target, option, names, values):
        """statement_2 : statement_3
statement_2 : statement_3
{$$ = new_node_1(STATEMENT_2,$1);}
            | statement_3 i_jj_stag_bo
{$$ = new_node_2(STATEMENT_2,$1,$2);}
            | statement_3 i_jj_stag_bo statement_2
{$$ = new_node_3(STATEMENT_2,$1,$2,$3);}
"""
        print "on_statement_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_i_jj_stag_bo(self, target, option, names, values):
        """i_jj_stag_bo : PRIVATE_I_BO I joik stag BO free_seq
i_jj_stag_bo : PRIVATE_I_BO I joik stag BO free_seq
{$$ = new_node_5(I_JJ_STAG_BO,$2,$3,$4,$5,$6);}
             | PRIVATE_I_BO I joik stag BO
{$$ = new_node_4(I_JJ_STAG_BO,$2,$3,$4,$5);}
             | PRIVATE_I_BO I joik      BO free_seq
{$$ = new_node_4(I_JJ_STAG_BO,$2,$3,$4,$5);}
             | PRIVATE_I_BO I joik      BO
{$$ = new_node_3(I_JJ_STAG_BO,$2,$3,$4);}
             | PRIVATE_I_BO I jek  stag BO free_seq
{$$ = new_node_5(I_JJ_STAG_BO,$2,$3,$4,$5,$6);}
             | PRIVATE_I_BO I jek  stag BO
{$$ = new_node_4(I_JJ_STAG_BO,$2,$3,$4,$5);}
             | PRIVATE_I_BO I jek       BO free_seq
{$$ = new_node_4(I_JJ_STAG_BO,$2,$3,$4,$5);}
             | PRIVATE_I_BO I jek       BO
{$$ = new_node_3(I_JJ_STAG_BO,$2,$3,$4);}
             | PRIVATE_I_BO I      stag BO free_seq
{$$ = new_node_4(I_JJ_STAG_BO,$2,$3,$4,$5);}
             | PRIVATE_I_BO I      stag BO
{$$ = new_node_3(I_JJ_STAG_BO,$2,$3,$4);}
             | PRIVATE_I_BO I           BO free_seq
{$$ = new_node_3(I_JJ_STAG_BO,$2,$3,$4);}
             | PRIVATE_I_BO I           BO
{$$ = new_node_2(I_JJ_STAG_BO,$2,$3);}
"""
        print "on_i_jj_stag_bo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_statement_3(self, target, option, names, values):
        """statement_3 : sentence
statement_3 : sentence
{$$ = new_node_1(STATEMENT_3,$1);}
            | tag TUhE free_seq text_1 TUhU free_seq
{$$ = new_node_6(STATEMENT_3,$1,$2,$3,$4,$5,$6);}
            | tag TUhE free_seq text_1 TUhU
{$$ = new_node_5(STATEMENT_3,$1,$2,$3,$4,$5);}
            | tag TUhE          text_1 TUhU free_seq
{$$ = new_node_5(STATEMENT_3,$1,$2,$3,$4,$5);}
            | tag TUhE          text_1 TUhU
{$$ = new_node_4(STATEMENT_3,$1,$2,$3,$4);}
            |     TUhE free_seq text_1 TUhU free_seq
{$$ = new_node_5(STATEMENT_3,$1,$2,$3,$4,$5);}
            |     TUhE free_seq text_1 TUhU
{$$ = new_node_4(STATEMENT_3,$1,$2,$3,$4);}
            |     TUhE          text_1 TUhU free_seq
{$$ = new_node_4(STATEMENT_3,$1,$2,$3,$4);}
            |     TUhE          text_1 TUhU
{$$ = new_node_3(STATEMENT_3,$1,$2,$3);}
"""
        print "on_statement_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_fragment(self, target, option, names, values):
        """fragment : ek free_seq
fragment : ek free_seq
{$$ = new_node_2(FRAGMENT,$1,$2);}
         | ek
{$$ = new_node_1(FRAGMENT,$1);}
         | gihek free_seq
{$$ = new_node_2(FRAGMENT,$1,$2);}
         | gihek
{$$ = new_node_1(FRAGMENT,$1);}
         | quantifier
{$$ = new_node_1(FRAGMENT,$1);}
         | NA free_seq
{$$ = new_node_2(FRAGMENT,$1,$2);}
         | NA
{$$ = new_node_1(FRAGMENT,$1);}
         | terms VAU free_seq
{$$ = new_node_3(FRAGMENT,$1,$2,$3);}
         | terms VAU
{$$ = new_node_2(FRAGMENT,$1,$2);}
         | prenex
{$$ = new_node_1(FRAGMENT,$1);}
         | relative_clauses
{$$ = new_node_1(FRAGMENT,$1);}
         | links
{$$ = new_node_1(FRAGMENT,$1);}
         | linkargs
{$$ = new_node_1(FRAGMENT,$1);}
"""
        print "on_fragment: got %s %s %s %s" % (target, option, names, values)
        return

    def on_prenex(self, target, option, names, values):
        """prenex : terms ZOhU free_seq
prenex : terms ZOhU free_seq
{$$ = new_node_3(PRENEX,$1,$2,$3);}
       | terms ZOhU
{$$ = new_node_2(PRENEX,$1,$2);}
"""
        print "on_prenex: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sentence(self, target, option, names, values):
        """sentence : terms CU free_seq bridi_tail
sentence : terms CU free_seq bridi_tail
{$$ = new_node_4(SENTENCE,$1,$2,$3,$4);}
         | terms CU          bridi_tail
{$$ = new_node_3(SENTENCE,$1,$2,$3);}
         | no_cu_sentence
{$$ = new_node_1(SENTENCE,$1);}
         | observative_sentence
{$$ = new_node_1(SENTENCE,$1);}
         | terms PRIVATE_START_GIHEK 
{
 fprintf(stderr, "Missing selbri before GIhA at line %d column %d\n",
         @2.first_line, @2.first_column);
 error_advance(0);
 $$ = $1;
 YYERROR;
}
         | terms PRIVATE_GIHEK_KE 
{
 fprintf(stderr, "Missing selbri before GIhA at line %d column %d\n",
         @2.first_line, @2.first_column);
 error_advance(0);
 $$ = $1;
 YYERROR;
}
         | terms PRIVATE_GIHEK_BO 
{
 fprintf(stderr, "Missing selbri before GIhA at line %d column %d\n",
         @2.first_line, @2.first_column);
 error_advance(0);
 $$ = $1;
 YYERROR;
}
"""
        print "on_sentence: got %s %s %s %s" % (target, option, names, values)
        return

    def on_no_cu_sentence(self, target, option, names, values):
        """no_cu_sentence : IMPOSSIBLE_TOKEN
no_cu_sentence : IMPOSSIBLE_TOKEN
{$$ = new_node_1(NO_CU_SENTENCE,$1);}
"""
        print "on_no_cu_sentence: got %s %s %s %s" % (target, option, names, values)
        return

    def on_observative_sentence(self, target, option, names, values):
        """observative_sentence : bridi_tail
observative_sentence : bridi_tail
{$$ = new_node_1(OBSERVATIVE_SENTENCE,$1);}
"""
        print "on_observative_sentence: got %s %s %s %s" % (target, option, names, values)
        return

    def on_subsentence(self, target, option, names, values):
        """subsentence : sentence
subsentence : sentence
{$$ = new_node_1(SUBSENTENCE,$1);}
            | prenex subsentence
{$$ = new_node_2(SUBSENTENCE,$1,$2);}
"""
        print "on_subsentence: got %s %s %s %s" % (target, option, names, values)
        return

    def on_bridi_tail(self, target, option, names, values):
        """bridi_tail : bridi_tail_1
bridi_tail : bridi_tail_1
{$$ = new_node_1(BRIDI_TAIL,$1);}
           | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE free_seq tail_terms
{$$ = new_node_8(BRIDI_TAIL,$1,$2,$3,$4,$5,$6,$7,$8);}
           | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE          tail_terms
{$$ = new_node_7(BRIDI_TAIL,$1,$2,$3,$4,$5,$6,$7);}
           | bridi_tail_1 gihek_stag_ke KE          bridi_tail KEhE free_seq tail_terms
{$$ = new_node_7(BRIDI_TAIL,$1,$2,$3,$4,$5,$6,$7);}
           | bridi_tail_1 gihek_stag_ke KE          bridi_tail KEhE          tail_terms
{$$ = new_node_6(BRIDI_TAIL,$1,$2,$3,$4,$5,$6);}
"""
        print "on_bridi_tail: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gihek_stag_ke(self, target, option, names, values):
        """gihek_stag_ke : PRIVATE_GIHEK_KE gihek stag
gihek_stag_ke : PRIVATE_GIHEK_KE gihek stag
{$$ = new_node_2(GIHEK_STAG_KE,$2,$3);}
              | PRIVATE_GIHEK_KE gihek
{$$ = new_node_1(GIHEK_STAG_KE,$2);}
"""
        print "on_gihek_stag_ke: got %s %s %s %s" % (target, option, names, values)
        return

    def on_bridi_tail_1(self, target, option, names, values):
        """bridi_tail_1 : bridi_tail_2
bridi_tail_1 : bridi_tail_2
{$$ = new_node_1(BRIDI_TAIL_1,$1);}
             | bridi_tail_1 gihek free_seq bridi_tail_2 tail_terms
{$$ = new_node_5(BRIDI_TAIL_1,$1,$2,$3,$4,$5);}
             | bridi_tail_1 gihek          bridi_tail_2 tail_terms
{$$ = new_node_4(BRIDI_TAIL_1,$1,$2,$3,$4);}
"""
        print "on_bridi_tail_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_bridi_tail_2(self, target, option, names, values):
        """bridi_tail_2 : bridi_tail_3
bridi_tail_2 : bridi_tail_3
{$$ = new_node_1(BRIDI_TAIL_2,$1);}
             | bridi_tail_2 gihek_stag_bo bridi_tail_2 tail_terms
{$$ = new_node_4(BRIDI_TAIL_2,$1,$2,$3,$4);}
"""
        print "on_bridi_tail_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gihek_stag_bo(self, target, option, names, values):
        """gihek_stag_bo : PRIVATE_GIHEK_BO gihek stag BO free_seq
gihek_stag_bo : PRIVATE_GIHEK_BO gihek stag BO free_seq
{$$ = new_node_4(GIHEK_STAG_BO,$2,$3,$4,$5);}
              | PRIVATE_GIHEK_BO gihek stag BO
{$$ = new_node_3(GIHEK_STAG_BO,$2,$3,$4);}
              | PRIVATE_GIHEK_BO gihek      BO free_seq
{$$ = new_node_3(GIHEK_STAG_BO,$2,$3,$4);}
              | PRIVATE_GIHEK_BO gihek      BO
{$$ = new_node_2(GIHEK_STAG_BO,$2,$3);}
"""
        print "on_gihek_stag_bo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_bridi_tail_3(self, target, option, names, values):
        """bridi_tail_3 : main_selbri tail_terms
bridi_tail_3 : main_selbri tail_terms
{$$ = new_node_2(BRIDI_TAIL_3,$1,$2);}
             | gek_sentence
{$$ = new_node_1(BRIDI_TAIL_3,$1);}
"""
        print "on_bridi_tail_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_main_selbri(self, target, option, names, values):
        """main_selbri : selbri
main_selbri : selbri
{$$ = new_node_1(MAIN_SELBRI,$1);}
"""
        print "on_main_selbri: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tail_terms(self, target, option, names, values):
        """tail_terms : terms VAU free_seq
tail_terms : terms VAU free_seq
{$$ = new_node_3(TAIL_TERMS,$1,$2,$3);}
           | terms VAU
{$$ = new_node_2(TAIL_TERMS,$1,$2);}
           |       VAU free_seq
{$$ = new_node_2(TAIL_TERMS,$1,$2);}
           |       VAU
{$$ = new_node_1(TAIL_TERMS,$1);}
"""
        print "on_tail_terms: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gek_sentence(self, target, option, names, values):
        """gek_sentence : gek subsentence gik subsentence tail_terms
gek_sentence : gek subsentence gik subsentence tail_terms
{$$ = new_node_5(GEK_SENTENCE,$1,$2,$3,$4,$5);}
             | tag KE free_seq gek_sentence KEhE free_seq
{$$ = new_node_6(GEK_SENTENCE,$1,$2,$3,$4,$5,$6);}
             | tag KE free_seq gek_sentence KEhE
{$$ = new_node_5(GEK_SENTENCE,$1,$2,$3,$4,$5);}
             | tag KE          gek_sentence KEhE free_seq
{$$ = new_node_5(GEK_SENTENCE,$1,$2,$3,$4,$5);}
             | tag KE          gek_sentence KEhE
{$$ = new_node_4(GEK_SENTENCE,$1,$2,$3,$4);}
             |     KE free_seq gek_sentence KEhE free_seq
{$$ = new_node_5(GEK_SENTENCE,$1,$2,$3,$4,$5);}
             |     KE free_seq gek_sentence KEhE
{$$ = new_node_4(GEK_SENTENCE,$1,$2,$3,$4);}
             |     KE          gek_sentence KEhE free_seq
{$$ = new_node_4(GEK_SENTENCE,$1,$2,$3,$4);}
             |     KE          gek_sentence KEhE
{$$ = new_node_3(GEK_SENTENCE,$1,$2,$3);}
             | NA free_seq gek_sentence
{$$ = new_node_3(GEK_SENTENCE,$1,$2,$3);}
             | NA          gek_sentence
{$$ = new_node_2(GEK_SENTENCE,$1,$2);}
"""
        print "on_gek_sentence: got %s %s %s %s" % (target, option, names, values)
        return

    def on_terms(self, target, option, names, values):
        """terms : terms_1
terms : terms_1
{$$ = new_node_1(TERMS,$1);}
      | terms terms_1
{$$ = new_node_2(TERMS,$1,$2);}
"""
        print "on_terms: got %s %s %s %s" % (target, option, names, values)
        return

    def on_terms_1(self, target, option, names, values):
        """terms_1 : terms_2
terms_1 : terms_2
{$$ = new_node_1(TERMS_1,$1);}
        | terms_1 PEhE free_seq joik free_seq terms_2
{$$ = new_node_6(TERMS_1,$1,$2,$3,$4,$5,$6);}
        | terms_1 PEhE free_seq joik          terms_2
{$$ = new_node_5(TERMS_1,$1,$2,$3,$4,$5);}
        | terms_1 PEhE free_seq jek  free_seq terms_2
{$$ = new_node_6(TERMS_1,$1,$2,$3,$4,$5,$6);}
        | terms_1 PEhE free_seq jek           terms_2
{$$ = new_node_5(TERMS_1,$1,$2,$3,$4,$5);}
        | terms_1 PEhE          joik free_seq terms_2
{$$ = new_node_5(TERMS_1,$1,$2,$3,$4,$5);}
        | terms_1 PEhE          joik          terms_2
{$$ = new_node_4(TERMS_1,$1,$2,$3,$4);}
        | terms_1 PEhE          jek  free_seq terms_2
{$$ = new_node_5(TERMS_1,$1,$2,$3,$4,$5);}
        | terms_1 PEhE          jek           terms_2
{$$ = new_node_4(TERMS_1,$1,$2,$3,$4);}
"""
        print "on_terms_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_terms_2(self, target, option, names, values):
        """terms_2 : term
terms_2 : term
{$$ = new_node_1(TERMS_2,$1);}
        | terms_2 CEhE free_seq term
{$$ = new_node_4(TERMS_2,$1,$2,$3,$4);}
        | terms_2 CEhE          term
{$$ = new_node_3(TERMS_2,$1,$2,$3);}
"""
        print "on_terms_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term(self, target, option, names, values):
        """term : term_plain_sumti
term : term_plain_sumti
{$$ = new_node_1(TERM,$1);}
     | term_tagged_sumti 
{$$ = new_node_1(TERM,$1);}
     | term_placed_sumti
{$$ = new_node_1(TERM,$1);}
     | term_floating_tense
{$$ = new_node_1(TERM,$1);}
     | termset
{$$ = new_node_1(TERM,$1);}
     | tagged_termset
{$$ = new_node_1(TERM,$1);}
     | term_floating_negate
{$$ = new_node_1(TERM,$1);}
     | term_other
{$$ = new_node_1(TERM,$1);}
"""
        print "on_term: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_plain_sumti(self, target, option, names, values):
        """term_plain_sumti : sumti
term_plain_sumti : sumti
{$$ = new_node_1(TERM_PLAIN_SUMTI,$1);}
"""
        print "on_term_plain_sumti: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_placed_sumti(self, target, option, names, values):
        """term_placed_sumti : FA free_seq sumti
term_placed_sumti : FA free_seq sumti
{$$ = new_node_3(TERM_PLACED_SUMTI,$1,$2,$3);}
                  | FA          sumti
{$$ = new_node_2(TERM_PLACED_SUMTI,$1,$2);}
"""
        print "on_term_placed_sumti: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_tagged_sumti(self, target, option, names, values):
        """term_tagged_sumti : tag sumti
term_tagged_sumti : tag sumti
{$$ = new_node_2(TERM_TAGGED_SUMTI,$1,$2);}
"""
        print "on_term_tagged_sumti: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tagged_termset(self, target, option, names, values):
        """tagged_termset : tag termset
tagged_termset : tag termset
{$$ = new_node_2(TAGGED_TERMSET,$1,$2);}
"""
        print "on_tagged_termset: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_floating_tense(self, target, option, names, values):
        """term_floating_tense : tag KU free_seq
term_floating_tense : tag KU free_seq
{$$ = new_node_3(TERM_FLOATING_TENSE,$1,$2,$3);}
                    | tag KU
{$$ = new_node_2(TERM_FLOATING_TENSE,$1,$2);}
"""
        print "on_term_floating_tense: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_floating_negate(self, target, option, names, values):
        """term_floating_negate : PRIVATE_NA_KU NA KU free_seq
term_floating_negate : PRIVATE_NA_KU NA KU free_seq
{$$ = new_node_3(TERM_FLOATING_NEGATE,$2,$3,$4);}
                     | PRIVATE_NA_KU NA KU
{$$ = new_node_2(TERM_FLOATING_NEGATE,$2,$3);}
"""
        print "on_term_floating_negate: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_other(self, target, option, names, values):
        """term_other : FA free_seq KU free_seq
term_other : FA free_seq KU free_seq
{$$ = new_node_4(TERM_OTHER,$1,$2,$3,$4);}
           | FA free_seq KU
{$$ = new_node_3(TERM_OTHER,$1,$2,$3);}
           | FA          KU free_seq
{$$ = new_node_3(TERM_OTHER,$1,$2,$3);}
           | FA          KU 
{$$ = new_node_2(TERM_OTHER,$1,$2);}
"""
        print "on_term_other: got %s %s %s %s" % (target, option, names, values)
        return

    def on_termset(self, target, option, names, values):
        """termset : termset_start gek termset_body gik termset_body
termset : termset_start gek termset_body gik termset_body
{$$ = new_node_5(TERMSET,$1,$2,$3,$4,$5);}
        | termset_start termset_body
{$$ = new_node_2(TERMSET,$1,$2);}
"""
        print "on_termset: got %s %s %s %s" % (target, option, names, values)
        return

    def on_termset_start(self, target, option, names, values):
        """termset_start : NUhI free_seq
termset_start : NUhI free_seq
{$$ = new_node_2(TERMSET_START,$1,$2);}
              | NUhI
{$$ = new_node_1(TERMSET_START,$1);}
"""
        print "on_termset_start: got %s %s %s %s" % (target, option, names, values)
        return

    def on_termset_body(self, target, option, names, values):
        """termset_body : terms NUhU free_seq
termset_body : terms NUhU free_seq
{$$ = new_node_3(TERMSET_BODY,$1,$2,$3);}
             | terms NUhU
{$$ = new_node_2(TERMSET_BODY,$1,$2);}
"""
        print "on_termset_body: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti(self, target, option, names, values):
        """sumti : sumti_1
sumti : sumti_1
{$$ = new_node_1(SUMTI,$1);}
      | sumti_1 VUhO free_seq relative_clauses
{$$ = new_node_4(SUMTI,$1,$2,$3,$4);}
      | sumti_1 VUhO          relative_clauses
{$$ = new_node_3(SUMTI,$1,$2,$3);}
"""
        print "on_sumti: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_1(self, target, option, names, values):
        """sumti_1 : sumti_2
sumti_1 : sumti_2
{$$ = new_node_1(SUMTI_1,$1);}
        | sumti_2 joik_ek_ke ke_sumti
{$$ = new_node_3(SUMTI_1,$1,$2,$3);}
"""
        print "on_sumti_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_ek_ke(self, target, option, names, values):
        """joik_ek_ke : PRIVATE_JOIK_KE joik stag
joik_ek_ke : PRIVATE_JOIK_KE joik stag
{$$ = new_node_2(JOIK_EK_KE,$2,$3);}
           | PRIVATE_JOIK_KE joik
{$$ = new_node_1(JOIK_EK_KE,$2);}
           | PRIVATE_EK_KE   ek   stag
{$$ = new_node_2(JOIK_EK_KE,$2,$3);}
           | PRIVATE_EK_KE   ek
{$$ = new_node_1(JOIK_EK_KE,$2);}
"""
        print "on_joik_ek_ke: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ke_sumti(self, target, option, names, values):
        """ke_sumti : KE free_seq sumti KEhE free_seq
ke_sumti : KE free_seq sumti KEhE free_seq
{$$ = new_node_5(KE_SUMTI,$1,$2,$3,$4,$5);}
         | KE free_seq sumti KEhE
{$$ = new_node_4(KE_SUMTI,$1,$2,$3,$4);}
         | KE          sumti KEhE free_seq
{$$ = new_node_4(KE_SUMTI,$1,$2,$3,$4);}
         | KE          sumti KEhE
{$$ = new_node_3(KE_SUMTI,$1,$2,$3);}
"""
        print "on_ke_sumti: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_2(self, target, option, names, values):
        """sumti_2 : sumti_3
sumti_2 : sumti_3
{$$ = new_node_1(SUMTI_2,$1);}
        | sumti_2 joik free_seq sumti_3
{$$ = new_node_4(SUMTI_2,$1,$2,$3,$4);}
        | sumti_2 joik          sumti_3
{$$ = new_node_3(SUMTI_2,$1,$2,$3);}
        | sumti_2 ek   free_seq sumti_3
{$$ = new_node_4(SUMTI_2,$1,$2,$3,$4);}
        | sumti_2 ek            sumti_3
{$$ = new_node_3(SUMTI_2,$1,$2,$3);}
"""
        print "on_sumti_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_3(self, target, option, names, values):
        """sumti_3 : sumti_4
sumti_3 : sumti_4
{$$ = new_node_1(SUMTI_3,$1);}
        | sumti_4 joik_ek_stag_bo sumti_3
{$$ = new_node_3(SUMTI_3,$1,$2,$3);}
"""
        print "on_sumti_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_ek_stag_bo(self, target, option, names, values):
        """joik_ek_stag_bo : PRIVATE_JOIK_BO joik stag BO free_seq
joik_ek_stag_bo : PRIVATE_JOIK_BO joik stag BO free_seq
{$$ = new_node_4(JOIK_EK_STAG_BO,$2,$3,$4,$5);}
                | PRIVATE_JOIK_BO joik stag BO
{$$ = new_node_3(JOIK_EK_STAG_BO,$2,$3,$4);}
                | PRIVATE_JOIK_BO joik      BO free_seq
{$$ = new_node_3(JOIK_EK_STAG_BO,$2,$3,$4);}
                | PRIVATE_JOIK_BO joik      BO
{$$ = new_node_2(JOIK_EK_STAG_BO,$2,$3);}
                | PRIVATE_EK_BO   ek   stag BO free_seq
{$$ = new_node_4(JOIK_EK_STAG_BO,$2,$3,$4,$5);}
                | PRIVATE_EK_BO   ek   stag BO
{$$ = new_node_3(JOIK_EK_STAG_BO,$2,$3,$4);}
                | PRIVATE_EK_BO   ek        BO free_seq
{$$ = new_node_3(JOIK_EK_STAG_BO,$2,$3,$4);}
                | PRIVATE_EK_BO   ek        BO
{$$ = new_node_2(JOIK_EK_STAG_BO,$2,$3);}
"""
        print "on_joik_ek_stag_bo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_4(self, target, option, names, values):
        """sumti_4 : sumti_5
sumti_4 : sumti_5
{$$ = new_node_1(SUMTI_4,$1);}
        | gek sumti gik sumti_4
{$$ = new_node_4(SUMTI_4,$1,$2,$3,$4);}
"""
        print "on_sumti_4: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_5(self, target, option, names, values):
        """sumti_5 : sumti_5a relative_clauses
sumti_5 : sumti_5a relative_clauses
{$$ = new_node_2(SUMTI_5,$1,$2);}
        | sumti_5a
{$$ = new_node_1(SUMTI_5,$1);}
        | sumti_5b relative_clauses
{$$ = new_node_2(SUMTI_5,$1,$2);}
        | sumti_5b
{$$ = new_node_1(SUMTI_5,$1);}
"""
        print "on_sumti_5: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_5a(self, target, option, names, values):
        """sumti_5a : quantifier sumti_6
sumti_5a : quantifier sumti_6
{$$ = new_node_2(SUMTI_5A,$1,$2);}
         |            sumti_6
{$$ = new_node_1(SUMTI_5A,$1);}
"""
        print "on_sumti_5a: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_5b(self, target, option, names, values):
        """sumti_5b : quantifier selbri KU free_seq
sumti_5b : quantifier selbri KU free_seq
{$$ = new_node_4(SUMTI_5B,$1,$2,$3,$4);}
         | quantifier selbri KU
{$$ = new_node_3(SUMTI_5B,$1,$2,$3);}
"""
        print "on_sumti_5b: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_6(self, target, option, names, values):
        """sumti_6 : lahe_sumti_6
sumti_6 : lahe_sumti_6
{$$ = new_node_1(SUMTI_6,$1);}
        | nahe_bo_sumti_6
{$$ = new_node_1(SUMTI_6,$1);}
        | KOhA    free_seq
{$$ = new_node_2(SUMTI_6,$1,$2);}
        | KOhA
{$$ = new_node_1(SUMTI_6,$1);}
        | lerfu_string BOI free_seq
{$$ = new_node_3(SUMTI_6,$1,$2,$3);}
        | lerfu_string BOI
{$$ = new_node_2(SUMTI_6,$1,$2);}
        | LE      free_seq sumti_tail KU free_seq
{$$ = new_node_5(SUMTI_6,$1,$2,$3,$4,$5);}
        | LE      free_seq sumti_tail KU
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LE               sumti_tail KU free_seq
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LE               sumti_tail KU
{$$ = new_node_3(SUMTI_6,$1,$2,$3);}
        | LA      free_seq sumti_tail KU free_seq
{$$ = new_node_5(SUMTI_6,$1,$2,$3,$4,$5);}
        | LA      free_seq sumti_tail KU
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LA               sumti_tail KU free_seq
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LA               sumti_tail KU
{$$ = new_node_3(SUMTI_6,$1,$2,$3);}
        | name_sumti_6
{$$ = new_node_1(SUMTI_6,$1);}
        | LI      free_seq mex LOhO free_seq
{$$ = new_node_5(SUMTI_6,$1,$2,$3,$4,$5);}
        | LI      free_seq mex LOhO
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LI               mex LOhO free_seq
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LI               mex LOhO
{$$ = new_node_3(SUMTI_6,$1,$2,$3);}
        | ZO free_seq 
{$$ = new_node_2(SUMTI_6,$1,$2);}
        | ZO          
{$$ = new_node_1(SUMTI_6,$1);}
        | LU text LIhU free_seq
{$$ = new_node_4(SUMTI_6,$1,$2,$3,$4);}
        | LU text LIhU
{$$ = new_node_3(SUMTI_6,$1,$2,$3);}
        | LOhU free_seq 
{$$ = new_node_2(SUMTI_6,$1,$2);}
        | LOhU          
{$$ = new_node_1(SUMTI_6,$1);}
        | ZOI  free_seq 
{$$ = new_node_2(SUMTI_6,$1,$2);}
        | ZOI           
{$$ = new_node_1(SUMTI_6,$1);}
"""
        print "on_sumti_6: got %s %s %s %s" % (target, option, names, values)
        return

    def on_lahe_sumti_6(self, target, option, names, values):
        """lahe_sumti_6 : LAhE    free_seq relative_clauses sumti LUhU free_seq
lahe_sumti_6 : LAhE    free_seq relative_clauses sumti LUhU free_seq
{$$ = new_node_6(LAHE_SUMTI_6,$1,$2,$3,$4,$5,$6);}
             | LAhE    free_seq relative_clauses sumti LUhU
{$$ = new_node_5(LAHE_SUMTI_6,$1,$2,$3,$4,$5);}
             | LAhE    free_seq                  sumti LUhU free_seq
{$$ = new_node_5(LAHE_SUMTI_6,$1,$2,$3,$4,$5);}
             | LAhE    free_seq                  sumti LUhU
{$$ = new_node_4(LAHE_SUMTI_6,$1,$2,$3,$4);}
             | LAhE             relative_clauses sumti LUhU free_seq
{$$ = new_node_5(LAHE_SUMTI_6,$1,$2,$3,$4,$5);}
             | LAhE             relative_clauses sumti LUhU
{$$ = new_node_4(LAHE_SUMTI_6,$1,$2,$3,$4);}
             | LAhE                              sumti LUhU free_seq
{$$ = new_node_4(LAHE_SUMTI_6,$1,$2,$3,$4);}
             | LAhE                              sumti LUhU
{$$ = new_node_3(LAHE_SUMTI_6,$1,$2,$3);}
"""
        print "on_lahe_sumti_6: got %s %s %s %s" % (target, option, names, values)
        return

    def on_nahe_bo_sumti_6(self, target, option, names, values):
        """nahe_bo_sumti_6 : PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti LUhU free_seq
nahe_bo_sumti_6 : PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti LUhU free_seq
{$$ = new_node_7(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6,$7,$8);}
                | PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti LUhU
{$$ = new_node_6(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6,$7);}
                | PRIVATE_NAhE_BO NAhE BO free_seq                  sumti LUhU free_seq
{$$ = new_node_6(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6,$7);}
                | PRIVATE_NAhE_BO NAhE BO free_seq                  sumti LUhU
{$$ = new_node_5(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6);}
                | PRIVATE_NAhE_BO NAhE BO          relative_clauses sumti LUhU free_seq
{$$ = new_node_6(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6,$7);}
                | PRIVATE_NAhE_BO NAhE BO          relative_clauses sumti LUhU
{$$ = new_node_5(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6);}
                | PRIVATE_NAhE_BO NAhE BO                           sumti LUhU free_seq
{$$ = new_node_5(NAHE_BO_SUMTI_6,$2,$3,$4,$5,$6);}
                | PRIVATE_NAhE_BO NAhE BO                           sumti LUhU
{$$ = new_node_4(NAHE_BO_SUMTI_6,$2,$3,$4,$5);}
"""
        print "on_nahe_bo_sumti_6: got %s %s %s %s" % (target, option, names, values)
        return

    def on_name_sumti_6(self, target, option, names, values):
        """name_sumti_6 : LA      free_seq relative_clauses CMENE_seq  free_seq
name_sumti_6 : LA      free_seq relative_clauses CMENE_seq  free_seq
{$$ = new_node_5(NAME_SUMTI_6,$1,$2,$3,$4,$5);}
             | LA      free_seq relative_clauses CMENE_seq
{$$ = new_node_4(NAME_SUMTI_6,$1,$2,$3,$4);}
             | LA      free_seq                  CMENE_seq  free_seq
{$$ = new_node_4(NAME_SUMTI_6,$1,$2,$3,$4);}
             | LA      free_seq                  CMENE_seq
{$$ = new_node_3(NAME_SUMTI_6,$1,$2,$3);}
             | LA               relative_clauses CMENE_seq  free_seq
{$$ = new_node_4(NAME_SUMTI_6,$1,$2,$3,$4);}
             | LA               relative_clauses CMENE_seq
{$$ = new_node_3(NAME_SUMTI_6,$1,$2,$3);}
             | LA                                CMENE_seq  free_seq
{$$ = new_node_3(NAME_SUMTI_6,$1,$2,$3);}
             | LA                                CMENE_seq
{$$ = new_node_2(NAME_SUMTI_6,$1,$2);}
"""
        print "on_name_sumti_6: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_tail(self, target, option, names, values):
        """sumti_tail : sumti_6 relative_clauses sumti_tail_1
sumti_tail : sumti_6 relative_clauses sumti_tail_1
{$$ = new_node_3(SUMTI_TAIL,$1,$2,$3);}
           | sumti_6                  sumti_tail_1
{$$ = new_node_2(SUMTI_TAIL,$1,$2);}
           |                          sumti_tail_1
{$$ = new_node_1(SUMTI_TAIL,$1);}
           |         relative_clauses sumti_tail_1
{$$ = new_node_2(SUMTI_TAIL,$1,$2);}
"""
        print "on_sumti_tail: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_tail_1(self, target, option, names, values):
        """sumti_tail_1 : sumti_tail_1A relative_clauses
sumti_tail_1 : sumti_tail_1A relative_clauses
{$$ = new_node_2(SUMTI_TAIL_1,$1,$2);}
             | sumti_tail_1A
{$$ = new_node_1(SUMTI_TAIL_1,$1);}
             | quantifier sumti
{$$ = new_node_2(SUMTI_TAIL_1,$1,$2);}
"""
        print "on_sumti_tail_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_sumti_tail_1A(self, target, option, names, values):
        """sumti_tail_1A : quantifier selbri
sumti_tail_1A : quantifier selbri
{$$ = new_node_2(SUMTI_TAIL_1A,$1,$2);}
              |            selbri
{$$ = new_node_1(SUMTI_TAIL_1A,$1);}
"""
        print "on_sumti_tail_1A: got %s %s %s %s" % (target, option, names, values)
        return

    def on_relative_clauses(self, target, option, names, values):
        """relative_clauses : relative_clause_seq
relative_clauses : relative_clause_seq
{$$ = new_node_1(RELATIVE_CLAUSES,$1);}
"""
        print "on_relative_clauses: got %s %s %s %s" % (target, option, names, values)
        return

    def on_relative_clause_seq(self, target, option, names, values):
        """relative_clause_seq : relative_clause
relative_clause_seq : relative_clause
{$$ = new_node_1(RELATIVE_CLAUSE_SEQ,$1);}
                    | relative_clause_seq ZIhE free_seq relative_clause
{$$ = new_node_4(RELATIVE_CLAUSE_SEQ,$1,$2,$3,$4);}
                    | relative_clause_seq ZIhE          relative_clause
{$$ = new_node_3(RELATIVE_CLAUSE_SEQ,$1,$2,$3);}
"""
        print "on_relative_clause_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_relative_clause(self, target, option, names, values):
        """relative_clause : term_relative_clause
relative_clause : term_relative_clause
{$$ = new_node_1(RELATIVE_CLAUSE,$1);}
                | full_relative_clause
{$$ = new_node_1(RELATIVE_CLAUSE,$1);}
"""
        print "on_relative_clause: got %s %s %s %s" % (target, option, names, values)
        return

    def on_term_relative_clause(self, target, option, names, values):
        """term_relative_clause : GOI free_seq term GEhU free_seq
term_relative_clause : GOI free_seq term GEhU free_seq
{$$ = new_node_5(TERM_RELATIVE_CLAUSE,$1,$2,$3,$4,$5);}
                     | GOI free_seq term GEhU
{$$ = new_node_4(TERM_RELATIVE_CLAUSE,$1,$2,$3,$4);}
                     | GOI          term GEhU free_seq
{$$ = new_node_4(TERM_RELATIVE_CLAUSE,$1,$2,$3,$4);}
                     | GOI          term GEhU
{$$ = new_node_3(TERM_RELATIVE_CLAUSE,$1,$2,$3);}
"""
        print "on_term_relative_clause: got %s %s %s %s" % (target, option, names, values)
        return

    def on_full_relative_clause(self, target, option, names, values):
        """full_relative_clause : NOI free_seq subsentence KUhO free_seq
full_relative_clause : NOI free_seq subsentence KUhO free_seq
{$$ = new_node_5(FULL_RELATIVE_CLAUSE,$1,$2,$3,$4,$5);}
                     | NOI free_seq subsentence KUhO
{$$ = new_node_4(FULL_RELATIVE_CLAUSE,$1,$2,$3,$4);}
                     | NOI          subsentence KUhO free_seq
{$$ = new_node_4(FULL_RELATIVE_CLAUSE,$1,$2,$3,$4);}
                     | NOI          subsentence KUhO
{$$ = new_node_3(FULL_RELATIVE_CLAUSE,$1,$2,$3);}
"""
        print "on_full_relative_clause: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri(self, target, option, names, values):
        """selbri : tag selbri_1
selbri : tag selbri_1
{$$ = new_node_2(SELBRI,$1,$2);}
       |     selbri_1
{$$ = new_node_1(SELBRI,$1);}
"""
        print "on_selbri: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_1(self, target, option, names, values):
        """selbri_1 : selbri_2
selbri_1 : selbri_2
{$$ = new_node_1(SELBRI_1,$1);}
         | NA free_seq selbri
{$$ = new_node_3(SELBRI_1,$1,$2,$3);}
         | NA          selbri
{$$ = new_node_2(SELBRI_1,$1,$2);}
"""
        print "on_selbri_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_2(self, target, option, names, values):
        """selbri_2 : selbri_3 CO free_seq selbri_2
selbri_2 : selbri_3 CO free_seq selbri_2
{$$ = new_node_4(SELBRI_2,$1,$2,$3,$4);}
         | selbri_3 CO          selbri_2
{$$ = new_node_3(SELBRI_2,$1,$2,$3);}
         | selbri_3
{$$ = new_node_1(SELBRI_2,$1);}
"""
        print "on_selbri_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_3(self, target, option, names, values):
        """selbri_3 : selbri_3 selbri_4
selbri_3 : selbri_3 selbri_4
{$$ = new_node_2(SELBRI_3,$1,$2);}
         |          selbri_4
{$$ = new_node_1(SELBRI_3,$1);}
"""
        print "on_selbri_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_4(self, target, option, names, values):
        """selbri_4 : selbri_5
selbri_4 : selbri_5
{$$ = new_node_1(SELBRI_4,$1);}
         | selbri_4 joik_opt_ke free_seq selbri_5
{$$ = new_node_4(SELBRI_4,$1,$2,$3,$4);}
         | selbri_4 joik_opt_ke          selbri_5
{$$ = new_node_3(SELBRI_4,$1,$2,$3);}
         | selbri_4 jek_opt_ke  free_seq selbri_5
{$$ = new_node_4(SELBRI_4,$1,$2,$3,$4);}
         | selbri_4 jek_opt_ke           selbri_5
{$$ = new_node_3(SELBRI_4,$1,$2,$3);}
         | selbri_4 joik_stag_ke ke_selbri_3
{$$ = new_node_3(SELBRI_4,$1,$2,$3);}
"""
        print "on_selbri_4: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_stag_ke(self, target, option, names, values):
        """joik_stag_ke : PRIVATE_JOIK_KE joik stag
joik_stag_ke : PRIVATE_JOIK_KE joik stag
{$$ = new_node_2(JOIK_STAG_KE,$2,$3);}
"""
        print "on_joik_stag_ke: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ke_selbri_3(self, target, option, names, values):
        """ke_selbri_3 : KE free_seq selbri_3 KEhE free_seq
ke_selbri_3 : KE free_seq selbri_3 KEhE free_seq
{$$ = new_node_5(KE_SELBRI_3,$1,$2,$3,$4,$5);}
            | KE free_seq selbri_3 KEhE
{$$ = new_node_4(KE_SELBRI_3,$1,$2,$3,$4);}
            | KE          selbri_3 KEhE free_seq
{$$ = new_node_4(KE_SELBRI_3,$1,$2,$3,$4);}
            | KE          selbri_3 KEhE
{$$ = new_node_3(KE_SELBRI_3,$1,$2,$3);}
"""
        print "on_ke_selbri_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_5(self, target, option, names, values):
        """selbri_5 : selbri_6
selbri_5 : selbri_6
{$$ = new_node_1(SELBRI_5,$1);}
         | selbri_6 joik_jek_stag_bo selbri_5
{$$ = new_node_3(SELBRI_5,$1,$2,$3);}
"""
        print "on_selbri_5: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_jek_stag_bo(self, target, option, names, values):
        """joik_jek_stag_bo : PRIVATE_JOIK_BO joik stag BO free_seq
joik_jek_stag_bo : PRIVATE_JOIK_BO joik stag BO free_seq
{$$ = new_node_4(JOIK_JEK_STAG_BO,$2,$3,$4,$5);}
                 | PRIVATE_JOIK_BO joik stag BO
{$$ = new_node_3(JOIK_JEK_STAG_BO,$2,$3,$4);}
                 | PRIVATE_JOIK_BO joik      BO free_seq
{$$ = new_node_3(JOIK_JEK_STAG_BO,$2,$3,$4);}
                 | PRIVATE_JOIK_BO joik      BO
{$$ = new_node_2(JOIK_JEK_STAG_BO,$2,$3);}
                 | PRIVATE_JEK_BO  jek  stag BO free_seq
{$$ = new_node_4(JOIK_JEK_STAG_BO,$2,$3,$4,$5);}
                 | PRIVATE_JEK_BO  jek  stag BO
{$$ = new_node_3(JOIK_JEK_STAG_BO,$2,$3,$4);}
                 | PRIVATE_JEK_BO  jek       BO free_seq
{$$ = new_node_3(JOIK_JEK_STAG_BO,$2,$3,$4);}
                 | PRIVATE_JEK_BO  jek       BO
{$$ = new_node_2(JOIK_JEK_STAG_BO,$2,$3);}
"""
        print "on_joik_jek_stag_bo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_selbri_6(self, target, option, names, values):
        """selbri_6 : tanru_unit
selbri_6 : tanru_unit
{$$ = new_node_1(SELBRI_6,$1);}
         | tanru_unit BO free_seq selbri_6
{$$ = new_node_4(SELBRI_6,$1,$2,$3,$4);}
         | tanru_unit BO          selbri_6
{$$ = new_node_3(SELBRI_6,$1,$2,$3);}
         | NAhE free_seq guhek selbri gik selbri_6
{$$ = new_node_6(SELBRI_6,$1,$2,$3,$4,$5,$6);}
         | NAhE          guhek selbri gik selbri_6
{$$ = new_node_5(SELBRI_6,$1,$2,$3,$4,$5);}
         |               guhek selbri gik selbri_6
{$$ = new_node_4(SELBRI_6,$1,$2,$3,$4);}
"""
        print "on_selbri_6: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tanru_unit(self, target, option, names, values):
        """tanru_unit : tanru_unit_1
tanru_unit : tanru_unit_1
{$$ = new_node_1(TANRU_UNIT,$1);}
           | tanru_unit CEI free_seq tanru_unit_1
{$$ = new_node_4(TANRU_UNIT,$1,$2,$3,$4);}
           | tanru_unit CEI          tanru_unit_1
{$$ = new_node_3(TANRU_UNIT,$1,$2,$3);}
"""
        print "on_tanru_unit: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tanru_unit_1(self, target, option, names, values):
        """tanru_unit_1 : tanru_unit_2
tanru_unit_1 : tanru_unit_2
{$$ = new_node_1(TANRU_UNIT_1,$1);}
             | tanru_unit_2 linkargs
{$$ = new_node_2(TANRU_UNIT_1,$1,$2);}
"""
        print "on_tanru_unit_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tanru_unit_2(self, target, option, names, values):
        """tanru_unit_2      : BRIVLA free_seq
tanru_unit_2      : BRIVLA free_seq
{$$ = new_node_2(TANRU_UNIT_2,$1,$2);}
                  | BRIVLA
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | GOhA RAhO free_seq
{$$ = new_node_3(TANRU_UNIT_2,$1,$2,$3);}
                  | GOhA RAhO
{$$ = new_node_2(TANRU_UNIT_2,$1,$2);}
                  | GOhA      free_seq
{$$ = new_node_2(TANRU_UNIT_2,$1,$2);}
                  | GOhA
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | ke_selbri3_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | ME free_seq sumti    MEhU free_seq MOI free_seq
{$$ = new_node_7(TANRU_UNIT_2,$1,$2,$3,$4,$5,$6,$7);}
                  | ME free_seq sumti    MEhU free_seq MOI
{$$ = new_node_6(TANRU_UNIT_2,$1,$2,$3,$4,$5,$6);}
                  | ME free_seq sumti    MEhU free_seq
{$$ = new_node_5(TANRU_UNIT_2,$1,$2,$3,$4,$5);}
                  | ME free_seq sumti    MEhU          MOI free_seq
{$$ = new_node_6(TANRU_UNIT_2,$1,$2,$3,$4,$5,$6);}
                  | ME free_seq sumti    MEhU          MOI
{$$ = new_node_5(TANRU_UNIT_2,$1,$2,$3,$4,$5);}
                  | ME free_seq sumti    MEhU
{$$ = new_node_4(TANRU_UNIT_2,$1,$2,$3,$4);}
                  | ME          sumti    MEhU free_seq MOI free_seq
{$$ = new_node_6(TANRU_UNIT_2,$1,$2,$3,$4,$5,$6);}
                  | ME          sumti    MEhU free_seq MOI
{$$ = new_node_5(TANRU_UNIT_2,$1,$2,$3,$4,$5);}
                  | ME          sumti    MEhU free_seq
{$$ = new_node_4(TANRU_UNIT_2,$1,$2,$3,$4);}
                  | ME          sumti    MEhU          MOI free_seq
{$$ = new_node_5(TANRU_UNIT_2,$1,$2,$3,$4,$5);}
                  | ME          sumti    MEhU          MOI
{$$ = new_node_4(TANRU_UNIT_2,$1,$2,$3,$4);}
                  | ME          sumti    MEhU
{$$ = new_node_3(TANRU_UNIT_2,$1,$2,$3);}
                  | number_moi_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | NUhA free_seq mex_operator
{$$ = new_node_3(TANRU_UNIT_2,$1,$2,$3);}
                  | NUhA          mex_operator
{$$ = new_node_2(TANRU_UNIT_2,$1,$2);}
                  | se_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | jai_tag_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | jai_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | ZEI 
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | nahe_tu2
{$$ = new_node_1(TANRU_UNIT_2,$1);}
                  | abstraction
{$$ = new_node_1(TANRU_UNIT_2,$1);}
"""
        print "on_tanru_unit_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ke_selbri3_tu2(self, target, option, names, values):
        """ke_selbri3_tu2 : KE free_seq selbri_3 KEhE free_seq
ke_selbri3_tu2 : KE free_seq selbri_3 KEhE free_seq
{$$ = new_node_5(KE_SELBRI3_TU2,$1,$2,$3,$4,$5);}
               | KE free_seq selbri_3 KEhE
{$$ = new_node_4(KE_SELBRI3_TU2,$1,$2,$3,$4);}
               | KE          selbri_3 KEhE free_seq
{$$ = new_node_4(KE_SELBRI3_TU2,$1,$2,$3,$4);}
               | KE          selbri_3 KEhE
{$$ = new_node_3(KE_SELBRI3_TU2,$1,$2,$3);}
"""
        print "on_ke_selbri3_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_number_moi_tu2(self, target, option, names, values):
        """number_moi_tu2 : PRIVATE_NUMBER_MOI number       MOI free_seq
number_moi_tu2 : PRIVATE_NUMBER_MOI number       MOI free_seq
{$$ = new_node_3(NUMBER_MOI_TU2,$2,$3,$4);}
               | PRIVATE_NUMBER_MOI number       MOI
{$$ = new_node_2(NUMBER_MOI_TU2,$2,$3);}
               | PRIVATE_NUMBER_MOI lerfu_string MOI free_seq
{$$ = new_node_3(NUMBER_MOI_TU2,$2,$3,$4);}
               | PRIVATE_NUMBER_MOI lerfu_string MOI
{$$ = new_node_2(NUMBER_MOI_TU2,$2,$3);}
"""
        print "on_number_moi_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_se_tu2(self, target, option, names, values):
        """se_tu2 : SE free_seq tanru_unit_2
se_tu2 : SE free_seq tanru_unit_2
{$$ = new_node_3(SE_TU2,$1,$2,$3);}
       | SE          tanru_unit_2
{$$ = new_node_2(SE_TU2,$1,$2);}
"""
        print "on_se_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_jai_tag_tu2(self, target, option, names, values):
        """jai_tag_tu2 : JAI free_seq tag tanru_unit_2
jai_tag_tu2 : JAI free_seq tag tanru_unit_2
{$$ = new_node_4(JAI_TAG_TU2,$1,$2,$3,$4);}
            | JAI          tag tanru_unit_2
{$$ = new_node_3(JAI_TAG_TU2,$1,$2,$3);}
"""
        print "on_jai_tag_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_jai_tu2(self, target, option, names, values):
        """jai_tu2 : JAI free_seq     tanru_unit_2
jai_tu2 : JAI free_seq     tanru_unit_2
{$$ = new_node_3(JAI_TU2,$1,$2,$3);}
        | JAI              tanru_unit_2
{$$ = new_node_2(JAI_TU2,$1,$2);}
"""
        print "on_jai_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_nahe_tu2(self, target, option, names, values):
        """nahe_tu2 : NAhE free_seq tanru_unit_2
nahe_tu2 : NAhE free_seq tanru_unit_2
{$$ = new_node_3(NAHE_TU2,$1,$2,$3);}
         | NAhE          tanru_unit_2
{$$ = new_node_2(NAHE_TU2,$1,$2);}
"""
        print "on_nahe_tu2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_abstraction(self, target, option, names, values):
        """abstraction : nu_nai_seq subsentence KEI free_seq
abstraction : nu_nai_seq subsentence KEI free_seq
{$$ = new_node_4(ABSTRACTION,$1,$2,$3,$4);}
            | nu_nai_seq subsentence KEI
{$$ = new_node_3(ABSTRACTION,$1,$2,$3);}
"""
        print "on_abstraction: got %s %s %s %s" % (target, option, names, values)
        return

    def on_nu_nai_seq(self, target, option, names, values):
        """nu_nai_seq : NU NAI free_seq
nu_nai_seq : NU NAI free_seq
{$$ = new_node_3(NU_NAI_SEQ,$1,$2,$3);}
           | NU     free_seq
{$$ = new_node_2(NU_NAI_SEQ,$1,$2);}
           | NU NAI
{$$ = new_node_2(NU_NAI_SEQ,$1,$2);}
           | NU
{$$ = new_node_1(NU_NAI_SEQ,$1);}
           | nu_nai_seq joik free_seq NU NAI free_seq
{$$ = new_node_6(NU_NAI_SEQ,$1,$2,$3,$4,$5,$6);}
           | nu_nai_seq joik free_seq NU NAI
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq joik free_seq NU     free_seq
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq joik free_seq NU
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq joik          NU NAI free_seq
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq joik          NU NAI
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq joik          NU     free_seq
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq joik          NU
{$$ = new_node_3(NU_NAI_SEQ,$1,$2,$3);}
           | nu_nai_seq jek  free_seq NU NAI free_seq
{$$ = new_node_6(NU_NAI_SEQ,$1,$2,$3,$4,$5,$6);}
           | nu_nai_seq jek  free_seq NU NAI
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq jek  free_seq NU     free_seq
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq jek  free_seq NU
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq jek           NU NAI free_seq
{$$ = new_node_5(NU_NAI_SEQ,$1,$2,$3,$4,$5);}
           | nu_nai_seq jek           NU NAI
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq jek           NU     free_seq
{$$ = new_node_4(NU_NAI_SEQ,$1,$2,$3,$4);}
           | nu_nai_seq jek           NU
{$$ = new_node_3(NU_NAI_SEQ,$1,$2,$3);}
"""
        print "on_nu_nai_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_linkargs(self, target, option, names, values):
        """linkargs : BE free_seq term links BEhO free_seq
linkargs : BE free_seq term links BEhO free_seq
{$$ = new_node_6(LINKARGS,$1,$2,$3,$4,$5,$6);}
         | BE free_seq term links BEhO
{$$ = new_node_5(LINKARGS,$1,$2,$3,$4,$5);}
         | BE          term links BEhO free_seq
{$$ = new_node_5(LINKARGS,$1,$2,$3,$4,$5);}
         | BE          term links BEhO
{$$ = new_node_4(LINKARGS,$1,$2,$3,$4);}
         | BE free_seq term       BEhO free_seq
{$$ = new_node_5(LINKARGS,$1,$2,$3,$4,$5);}
         | BE free_seq term       BEhO
{$$ = new_node_4(LINKARGS,$1,$2,$3,$4);}
         | BE          term       BEhO free_seq
{$$ = new_node_4(LINKARGS,$1,$2,$3,$4);}
         | BE          term       BEhO
{$$ = new_node_3(LINKARGS,$1,$2,$3);}
"""
        print "on_linkargs: got %s %s %s %s" % (target, option, names, values)
        return

    def on_links(self, target, option, names, values):
        """links : BEI free_seq term links
links : BEI free_seq term links
{$$ = new_node_4(LINKS,$1,$2,$3,$4);}
      | BEI          term links
{$$ = new_node_3(LINKS,$1,$2,$3);}
      | BEI free_seq term
{$$ = new_node_3(LINKS,$1,$2,$3);}
      | BEI          term
{$$ = new_node_2(LINKS,$1,$2);}
"""
        print "on_links: got %s %s %s %s" % (target, option, names, values)
        return

    def on_quantifier(self, target, option, names, values):
        """quantifier : number BOI free_seq
quantifier : number BOI free_seq
{$$ = new_node_3(QUANTIFIER,$1,$2,$3);}
           | number BOI
{$$ = new_node_2(QUANTIFIER,$1,$2);}
           | VEI free_seq mex VEhO free_seq
{$$ = new_node_5(QUANTIFIER,$1,$2,$3,$4,$5);}
           | VEI free_seq mex VEhO
{$$ = new_node_4(QUANTIFIER,$1,$2,$3,$4);}
           | VEI          mex VEhO free_seq
{$$ = new_node_4(QUANTIFIER,$1,$2,$3,$4);}
           | VEI          mex VEhO
{$$ = new_node_3(QUANTIFIER,$1,$2,$3);}
"""
        print "on_quantifier: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex(self, target, option, names, values):
        """mex : mex_infix
mex : mex_infix
{$$ = new_node_1(MEX,$1);}
    | mex_rp
{$$ = new_node_1(MEX,$1);}
"""
        print "on_mex: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_rp(self, target, option, names, values):
        """mex_rp : FUhA free_seq rp_expression
mex_rp : FUhA free_seq rp_expression
{$$ = new_node_3(MEX_RP,$1,$2,$3);}
       | FUhA          rp_expression
{$$ = new_node_2(MEX_RP,$1,$2);}
"""
        print "on_mex_rp: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_infix(self, target, option, names, values):
        """mex_infix : mex_1
mex_infix : mex_1
{$$ = new_node_1(MEX_INFIX,$1);}
          | mex_infix operator mex_1
{$$ = new_node_3(MEX_INFIX,$1,$2,$3);}
"""
        print "on_mex_infix: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_1(self, target, option, names, values):
        """mex_1 : mex_2
mex_1 : mex_2
{$$ = new_node_1(MEX_1,$1);}
      | mex_2 BIhE free_seq operator mex_1
{$$ = new_node_5(MEX_1,$1,$2,$3,$4,$5);}
      | mex_2 BIhE          operator mex_1
{$$ = new_node_4(MEX_1,$1,$2,$3,$4);}
"""
        print "on_mex_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_2(self, target, option, names, values):
        """mex_2 : operand
mex_2 : operand
{$$ = new_node_1(MEX_2,$1);}
      | PEhO free_seq operator mex_2_seq KUhE free_seq
{$$ = new_node_6(MEX_2,$1,$2,$3,$4,$5,$6);}
      | PEhO free_seq operator mex_2_seq KUhE
{$$ = new_node_5(MEX_2,$1,$2,$3,$4,$5);}
      | PEhO          operator mex_2_seq KUhE free_seq
{$$ = new_node_5(MEX_2,$1,$2,$3,$4,$5);}
      | PEhO          operator mex_2_seq KUhE
{$$ = new_node_4(MEX_2,$1,$2,$3,$4);}
      |               operator mex_2_seq KUhE free_seq
{$$ = new_node_4(MEX_2,$1,$2,$3,$4);}
      |               operator mex_2_seq KUhE
{$$ = new_node_3(MEX_2,$1,$2,$3);}
"""
        print "on_mex_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_2_seq(self, target, option, names, values):
        """mex_2_seq :           mex_2
mex_2_seq :           mex_2
{$$ = new_node_1(MEX_2_SEQ,$1);}
          | mex_2_seq mex_2
{$$ = new_node_2(MEX_2_SEQ,$1,$2);}
"""
        print "on_mex_2_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_rp_expression(self, target, option, names, values):
        """rp_expression : rp_expression rp_expression operator
rp_expression : rp_expression rp_expression operator
{$$ = new_node_3(RP_EXPRESSION,$1,$2,$3);}
              | operand       rp_expression operator
{$$ = new_node_3(RP_EXPRESSION,$1,$2,$3);}
              | rp_expression operand       operator
{$$ = new_node_3(RP_EXPRESSION,$1,$2,$3);}
              | operand       operand       operator
{$$ = new_node_3(RP_EXPRESSION,$1,$2,$3);}
"""
        print "on_rp_expression: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operator(self, target, option, names, values):
        """operator : operator_1
operator : operator_1
{$$ = new_node_1(OPERATOR,$1);}
         | operator joik_opt_ke free_seq operator_1
{$$ = new_node_4(OPERATOR,$1,$2,$3,$4);}
         | operator joik_opt_ke          operator_1
{$$ = new_node_3(OPERATOR,$1,$2,$3);}
         | operator jek_opt_ke  free_seq operator_1
{$$ = new_node_4(OPERATOR,$1,$2,$3,$4);}
         | operator jek_opt_ke           operator_1
{$$ = new_node_3(OPERATOR,$1,$2,$3);}
         | operator joik_stag_ke ke_operator
{$$ = new_node_3(OPERATOR,$1,$2,$3);}
"""
        print "on_operator: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ke_operator(self, target, option, names, values):
        """ke_operator : KE free_seq operator KEhE free_seq
ke_operator : KE free_seq operator KEhE free_seq
{$$ = new_node_5(KE_OPERATOR,$1,$2,$3,$4,$5);}
            | KE free_seq operator KEhE
{$$ = new_node_4(KE_OPERATOR,$1,$2,$3,$4);}
            | KE          operator KEhE free_seq
{$$ = new_node_4(KE_OPERATOR,$1,$2,$3,$4);}
            | KE          operator KEhE
{$$ = new_node_3(KE_OPERATOR,$1,$2,$3);}
"""
        print "on_ke_operator: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operator_1(self, target, option, names, values):
        """operator_1 : operator_2
operator_1 : operator_2
{$$ = new_node_1(OPERATOR_1,$1);}
           | guhek operator_1 gik operator_2
{$$ = new_node_4(OPERATOR_1,$1,$2,$3,$4);}
           | operator_2 joik_jek_stag_bo operator_1
{$$ = new_node_3(OPERATOR_1,$1,$2,$3);}
"""
        print "on_operator_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operator_2(self, target, option, names, values):
        """operator_2 : mex_operator
operator_2 : mex_operator
{$$ = new_node_1(OPERATOR_2,$1);}
           | KE free_seq operator KEhE free_seq
{$$ = new_node_5(OPERATOR_2,$1,$2,$3,$4,$5);}
           | KE free_seq operator KEhE
{$$ = new_node_4(OPERATOR_2,$1,$2,$3,$4);}
           | KE          operator KEhE free_seq
{$$ = new_node_4(OPERATOR_2,$1,$2,$3,$4);}
           | KE          operator KEhE
{$$ = new_node_3(OPERATOR_2,$1,$2,$3);}
"""
        print "on_operator_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_mex_operator(self, target, option, names, values):
        """mex_operator : SE free_seq mex_operator
mex_operator : SE free_seq mex_operator
{$$ = new_node_3(MEX_OPERATOR,$1,$2,$3);}
             | SE          mex_operator
{$$ = new_node_2(MEX_OPERATOR,$1,$2);}
             | NAhE free_seq mex_operator
{$$ = new_node_3(MEX_OPERATOR,$1,$2,$3);}
             | NAhE          mex_operator
{$$ = new_node_2(MEX_OPERATOR,$1,$2);}
             | MAhO free_seq mex TEhU free_seq
{$$ = new_node_5(MEX_OPERATOR,$1,$2,$3,$4,$5);}
             | MAhO free_seq mex TEhU
{$$ = new_node_4(MEX_OPERATOR,$1,$2,$3,$4);}
             | MAhO          mex TEhU free_seq
{$$ = new_node_4(MEX_OPERATOR,$1,$2,$3,$4);}
             | MAhO          mex TEhU
{$$ = new_node_3(MEX_OPERATOR,$1,$2,$3);}
             | NAhU free_seq selbri TEhU free_seq
{$$ = new_node_5(MEX_OPERATOR,$1,$2,$3,$4,$5);}
             | NAhU free_seq selbri TEhU
{$$ = new_node_4(MEX_OPERATOR,$1,$2,$3,$4);}
             | NAhU          selbri TEhU free_seq
{$$ = new_node_4(MEX_OPERATOR,$1,$2,$3,$4);}
             | NAhU          selbri TEhU
{$$ = new_node_3(MEX_OPERATOR,$1,$2,$3);}
             | VUhU free_seq
{$$ = new_node_2(MEX_OPERATOR,$1,$2);}
             | VUhU
{$$ = new_node_1(MEX_OPERATOR,$1);}
"""
        print "on_mex_operator: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operand(self, target, option, names, values):
        """operand : operand_1
operand : operand_1
{$$ = new_node_1(OPERAND,$1);}
        | operand_1 joik_ek_ke ke_operand
{$$ = new_node_3(OPERAND,$1,$2,$3);}
"""
        print "on_operand: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ke_operand(self, target, option, names, values):
        """ke_operand : KE free_seq operand KEhE free_seq
ke_operand : KE free_seq operand KEhE free_seq
{$$ = new_node_5(KE_OPERAND,$1,$2,$3,$4,$5);}
           | KE free_seq operand KEhE
{$$ = new_node_4(KE_OPERAND,$1,$2,$3,$4);}
           | KE          operand KEhE free_seq
{$$ = new_node_4(KE_OPERAND,$1,$2,$3,$4);}
           | KE          operand KEhE
{$$ = new_node_3(KE_OPERAND,$1,$2,$3);}
"""
        print "on_ke_operand: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operand_1(self, target, option, names, values):
        """operand_1 : operand_2
operand_1 : operand_2
{$$ = new_node_1(OPERAND_1,$1);}
          | operand_1 joik free_seq operand_2
{$$ = new_node_4(OPERAND_1,$1,$2,$3,$4);}
          | operand_1 joik          operand_2
{$$ = new_node_3(OPERAND_1,$1,$2,$3);}
          | operand_1 jek  free_seq operand_2
{$$ = new_node_4(OPERAND_1,$1,$2,$3,$4);}
          | operand_1 jek           operand_2
{$$ = new_node_3(OPERAND_1,$1,$2,$3);}
"""
        print "on_operand_1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operand_2(self, target, option, names, values):
        """operand_2 : operand_3
operand_2 : operand_3
{$$ = new_node_1(OPERAND_2,$1);}
          | operand_3 joik_ek_stag_bo operand_2
{$$ = new_node_3(OPERAND_2,$1,$2,$3);}
"""
        print "on_operand_2: got %s %s %s %s" % (target, option, names, values)
        return

    def on_operand_3(self, target, option, names, values):
        """operand_3 : quantifier
operand_3 : quantifier
{$$ = new_node_1(OPERAND_3,$1);}
          | lerfu_string BOI free_seq
{$$ = new_node_3(OPERAND_3,$1,$2,$3);}
          | lerfu_string BOI
{$$ = new_node_2(OPERAND_3,$1,$2);}
          | NIhE free_seq selbri TEhU free_seq
{$$ = new_node_5(OPERAND_3,$1,$2,$3,$4,$5);}
          | NIhE free_seq selbri TEhU
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | NIhE          selbri TEhU free_seq
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | NIhE          selbri TEhU
{$$ = new_node_3(OPERAND_3,$1,$2,$3);}
          | MOhE free_seq sumti  TEhU free_seq
{$$ = new_node_5(OPERAND_3,$1,$2,$3,$4,$5);}
          | MOhE free_seq sumti  TEhU
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | MOhE          sumti  TEhU free_seq
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | MOhE          sumti  TEhU
{$$ = new_node_3(OPERAND_3,$1,$2,$3);}
          | JOhI free_seq mex_2_seq TEhU free_seq
{$$ = new_node_5(OPERAND_3,$1,$2,$3,$4,$5);}
          | JOhI free_seq mex_2_seq TEhU
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | JOhI          mex_2_seq TEhU free_seq
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | JOhI          mex_2_seq TEhU
{$$ = new_node_3(OPERAND_3,$1,$2,$3);}
          | gek operand gik operand_3
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | LAhE free_seq operand LUhU free_seq
{$$ = new_node_5(OPERAND_3,$1,$2,$3,$4,$5);}
          | LAhE free_seq operand LUhU
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | LAhE          operand LUhU free_seq
{$$ = new_node_4(OPERAND_3,$1,$2,$3,$4);}
          | LAhE          operand LUhU
{$$ = new_node_3(OPERAND_3,$1,$2,$3);}
          | PRIVATE_NAhE_BO NAhE BO free_seq operand LUhU free_seq
{$$ = new_node_6(OPERAND_3,$2,$3,$4,$5,$6,$7);}
          | PRIVATE_NAhE_BO NAhE BO free_seq operand LUhU
{$$ = new_node_5(OPERAND_3,$2,$3,$4,$5,$6);}
          | PRIVATE_NAhE_BO NAhE BO          operand LUhU free_seq
{$$ = new_node_5(OPERAND_3,$2,$3,$4,$5,$6);}
          | PRIVATE_NAhE_BO NAhE BO          operand LUhU
{$$ = new_node_4(OPERAND_3,$2,$3,$4,$5);}
"""
        print "on_operand_3: got %s %s %s %s" % (target, option, names, values)
        return

    def on_number(self, target, option, names, values):
        """number : inner_number
number : inner_number
{$$ = new_node_1(NUMBER,$1);}
"""
        print "on_number: got %s %s %s %s" % (target, option, names, values)
        return

    def on_inner_number(self, target, option, names, values):
        """inner_number : PA
inner_number : PA
{$$ = new_node_1(INNER_NUMBER,$1);}
             | inner_number PA
{$$ = new_node_2(INNER_NUMBER,$1,$2);}
             | inner_number lerfu_word
{$$ = new_node_2(INNER_NUMBER,$1,$2);}
"""
        print "on_inner_number: got %s %s %s %s" % (target, option, names, values)
        return

    def on_lerfu_string(self, target, option, names, values):
        """lerfu_string : lerfu_word
lerfu_string : lerfu_word
{$$ = new_node_1(LERFU_STRING,$1);}
             | lerfu_string PA
{$$ = new_node_2(LERFU_STRING,$1,$2);}
             | lerfu_string lerfu_word
{$$ = new_node_2(LERFU_STRING,$1,$2);}
"""
        print "on_lerfu_string: got %s %s %s %s" % (target, option, names, values)
        return

    def on_lerfu_word(self, target, option, names, values):
        """lerfu_word : BY
lerfu_word : BY
{$$ = new_node_1(LERFU_WORD,$1);}
           | BU 
{$$ = new_node_1(LERFU_WORD,$1);}
           | LAU lerfu_word
{$$ = new_node_2(LERFU_WORD,$1,$2);}
           | TEI lerfu_string FOI
{$$ = new_node_3(LERFU_WORD,$1,$2,$3);}
"""
        print "on_lerfu_word: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ek(self, target, option, names, values):
        """ek : PRIVATE_START_EK NA SE A NAI
ek : PRIVATE_START_EK NA SE A NAI
{$$ = new_node_4(EK,$2,$3,$4,$5);}
   | PRIVATE_START_EK NA SE A
{$$ = new_node_3(EK,$2,$3,$4);}
   | PRIVATE_START_EK NA    A NAI
{$$ = new_node_3(EK,$2,$3,$4);}
   | PRIVATE_START_EK NA    A
{$$ = new_node_2(EK,$2,$3);}
   | PRIVATE_START_EK    SE A NAI
{$$ = new_node_3(EK,$2,$3,$4);}
   | PRIVATE_START_EK    SE A
{$$ = new_node_2(EK,$2,$3);}
   | PRIVATE_START_EK       A NAI
{$$ = new_node_2(EK,$2,$3);}
   | PRIVATE_START_EK       A
{$$ = new_node_1(EK,$2);}
"""
        print "on_ek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gihek(self, target, option, names, values):
        """gihek : PRIVATE_START_GIHEK NA SE GIhA NAI
gihek : PRIVATE_START_GIHEK NA SE GIhA NAI
{$$ = new_node_4(GIHEK,$2,$3,$4,$5);}
      | PRIVATE_START_GIHEK NA SE GIhA
{$$ = new_node_3(GIHEK,$2,$3,$4);}
      | PRIVATE_START_GIHEK NA    GIhA NAI
{$$ = new_node_3(GIHEK,$2,$3,$4);}
      | PRIVATE_START_GIHEK NA    GIhA
{$$ = new_node_2(GIHEK,$2,$3);}
      | PRIVATE_START_GIHEK    SE GIhA NAI
{$$ = new_node_3(GIHEK,$2,$3,$4);}
      | PRIVATE_START_GIHEK    SE GIhA
{$$ = new_node_2(GIHEK,$2,$3);}
      | PRIVATE_START_GIHEK       GIhA NAI
{$$ = new_node_2(GIHEK,$2,$3);}
      | PRIVATE_START_GIHEK       GIhA
{$$ = new_node_1(GIHEK,$2);}
"""
        print "on_gihek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_jek(self, target, option, names, values):
        """jek : PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
jek : PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK,$2,$3,$4,$5);}
    | PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK,$2,$3,$4);}
    | PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK,$2,$3,$4);}
    | PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK,$2,$3);}
    | PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK,$2,$3,$4);}
    | PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK,$2,$3);}
    | PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK,$2,$3);}
    | PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK,$2);}
"""
        print "on_jek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_jek_opt_ke(self, target, option, names, values):
        """jek_opt_ke :                PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
jek_opt_ke :                PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK_OPT_KE,$2,$3,$4,$5);}
           |                PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$2,$3,$4);}
           |                PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$2,$3,$4);}
           |                PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$2,$3);}
           |                PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$2,$3,$4);}
           |                PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$2,$3);}
           |                PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$2,$3);}
           |                PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK_OPT_KE,$2);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK_OPT_KE,$3,$4,$5,$6);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$3,$4,$5);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$3,$4,$5);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$3,$4);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KE,$3,$4,$5);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$3,$4);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KE,$3,$4);}
           | PRIVATE_JEK_KE PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK_OPT_KE,$3);}
"""
        print "on_jek_opt_ke: got %s %s %s %s" % (target, option, names, values)
        return

    def on_jek_opt_kebo(self, target, option, names, values):
        """jek_opt_kebo :                PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
jek_opt_kebo :                PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK_OPT_KEBO,$2,$3,$4,$5);}
             |                PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$2,$3,$4);}
             |                PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$2,$3,$4);}
             |                PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$2,$3);}
             |                PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$2,$3,$4);}
             |                PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$2,$3);}
             |                PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$2,$3);}
             |                PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK_OPT_KEBO,$2);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK_OPT_KEBO,$3,$4,$5,$6);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_KE PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK_OPT_KEBO,$3);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
{$$ = new_node_4(JEK_OPT_KEBO,$3,$4,$5,$6);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK NA SE JA     PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK NA    JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK NA    JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK    SE JA NAI PRIVATE_END_JEK
{$$ = new_node_3(JEK_OPT_KEBO,$3,$4,$5);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK    SE JA     PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK       JA NAI PRIVATE_END_JEK
{$$ = new_node_2(JEK_OPT_KEBO,$3,$4);}
             | PRIVATE_JEK_BO PRIVATE_START_JEK       JA     PRIVATE_END_JEK
{$$ = new_node_1(JEK_OPT_KEBO,$3);}
"""
        print "on_jek_opt_kebo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik(self, target, option, names, values):
        """joik : PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
joik : PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK,$2,$3,$4);}
     | PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK,$2,$3);}
     | PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK,$2,$3);}
     | PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK,$2);}
     | PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK,$2,$3,$4);}
     | PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK,$2,$3);}
     | PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK,$2,$3);}
     | PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK,$2);}
     | PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK,$2,$3,$4,$5,$6);}
     | PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK,$2,$3,$4,$5);}
     | PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK,$2,$3,$4,$5);}
     | PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK,$2,$3,$4);}
"""
        print "on_joik: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_opt_ke(self, target, option, names, values):
        """joik_opt_ke :                 PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
joik_opt_ke :                 PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$2,$3,$4);}
            |                 PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$2,$3);}
            |                 PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$2,$3);}
            |                 PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KE,$2);}
            |                 PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$2,$3,$4);}
            |                 PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$2,$3);}
            |                 PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$2,$3);}
            |                 PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KE,$2);}
            |                 PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK_OPT_KE,$2,$3,$4,$5,$6);}
            |                 PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KE,$2,$3,$4,$5);}
            |                 PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KE,$2,$3,$4,$5);}
            |                 PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$2,$3,$4);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$3,$4,$5);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$3,$4);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$3,$4);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KE,$3);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$3,$4,$5);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$3,$4);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KE,$3,$4);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KE,$3);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK_OPT_KE,$3,$4,$5,$6,$7);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KE,$3,$4,$5,$6);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KE,$3,$4,$5,$6);}
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KE,$3,$4,$5);}
"""
        print "on_joik_opt_ke: got %s %s %s %s" % (target, option, names, values)
        return

    def on_joik_opt_kebo(self, target, option, names, values):
        """joik_opt_kebo :                 PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
joik_opt_kebo :                 PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$2,$3,$4);}
              |                 PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$2,$3);}
              |                 PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$2,$3);}
              |                 PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$2);}
              |                 PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$2,$3,$4);}
              |                 PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$2,$3);}
              |                 PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$2,$3);}
              |                 PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$2);}
              |                 PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK_OPT_KEBO,$2,$3,$4,$5,$6);}
              |                 PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$2,$3,$4,$5);}
              |                 PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$2,$3,$4,$5);}
              |                 PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$2,$3,$4);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$3);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$3);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK_OPT_KEBO,$3,$4,$5,$6,$7);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$3,$4,$5,$6);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$3,$4,$5,$6);}
              | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK      SE JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK      SE JOI           PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK         JOI  NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK         JOI           PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$3);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK      SE BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK      SE BIhI          PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK         BIhI NAI      PRIVATE_END_JOIK
{$$ = new_node_2(JOIK_OPT_KEBO,$3,$4);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK         BIhI          PRIVATE_END_JOIK
{$$ = new_node_1(JOIK_OPT_KEBO,$3);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_5(JOIK_OPT_KEBO,$3,$4,$5,$6,$7);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO SE BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$3,$4,$5,$6);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO    BIhI NAI GAhO PRIVATE_END_JOIK
{$$ = new_node_4(JOIK_OPT_KEBO,$3,$4,$5,$6);}
              | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO    BIhI     GAhO PRIVATE_END_JOIK
{$$ = new_node_3(JOIK_OPT_KEBO,$3,$4,$5);}
"""
        print "on_joik_opt_kebo: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gek(self, target, option, names, values):
        """gek : PRIVATE_START_GEK SE GA NAI free_seq
gek : PRIVATE_START_GEK SE GA NAI free_seq
{$$ = new_node_4(GEK,$2,$3,$4,$5);}
    | PRIVATE_START_GEK SE GA NAI
{$$ = new_node_3(GEK,$2,$3,$4);}
    | PRIVATE_START_GEK SE GA     free_seq
{$$ = new_node_3(GEK,$2,$3,$4);}
    | PRIVATE_START_GEK SE GA    
{$$ = new_node_2(GEK,$2,$3);}
    | PRIVATE_START_GEK    GA NAI free_seq
{$$ = new_node_3(GEK,$2,$3,$4);}
    | PRIVATE_START_GEK    GA NAI
{$$ = new_node_2(GEK,$2,$3);}
    | PRIVATE_START_GEK    GA     free_seq
{$$ = new_node_2(GEK,$2,$3);}
    | PRIVATE_START_GEK    GA    
{$$ = new_node_1(GEK,$2);}
    | PRIVATE_START_GEK joik GI free_seq
{$$ = new_node_3(GEK,$2,$3,$4);}
    | PRIVATE_START_GEK joik GI
{$$ = new_node_2(GEK,$2,$3);}
    | PRIVATE_START_GEK stag gik
{$$ = new_node_2(GEK,$2,$3);}
"""
        print "on_gek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_guhek(self, target, option, names, values):
        """guhek : PRIVATE_START_GUHEK SE GUhA NAI free_seq
guhek : PRIVATE_START_GUHEK SE GUhA NAI free_seq
{$$ = new_node_4(GUHEK,$2,$3,$4,$5);}
      | PRIVATE_START_GUHEK SE GUhA NAI
{$$ = new_node_3(GUHEK,$2,$3,$4);}
      | PRIVATE_START_GUHEK SE GUhA     free_seq
{$$ = new_node_3(GUHEK,$2,$3,$4);}
      | PRIVATE_START_GUHEK SE GUhA    
{$$ = new_node_2(GUHEK,$2,$3);}
      | PRIVATE_START_GUHEK    GUhA NAI free_seq
{$$ = new_node_3(GUHEK,$2,$3,$4);}
      | PRIVATE_START_GUHEK    GUhA NAI
{$$ = new_node_2(GUHEK,$2,$3);}
      | PRIVATE_START_GUHEK    GUhA     free_seq
{$$ = new_node_2(GUHEK,$2,$3);}
      | PRIVATE_START_GUHEK    GUhA    
{$$ = new_node_1(GUHEK,$2);}
"""
        print "on_guhek: got %s %s %s %s" % (target, option, names, values)
        return

    def on_gik(self, target, option, names, values):
        """gik : GI NAI free_seq
gik : GI NAI free_seq
{$$ = new_node_3(GIK,$1,$2,$3);}
    | GI NAI
{$$ = new_node_2(GIK,$1,$2);}
    | GI     free_seq
{$$ = new_node_2(GIK,$1,$2);}
    | GI
{$$ = new_node_1(GIK,$1);}
"""
        print "on_gik: got %s %s %s %s" % (target, option, names, values)
        return

    def on_tag(self, target, option, names, values):
        """tag : ctag
tag : ctag
{$$ = new_node_1(TAG,$1);}
    | stag
{$$ = new_node_1(TAG,$1);}
"""
        print "on_tag: got %s %s %s %s" % (target, option, names, values)
        return

    def on_ctag(self, target, option, names, values):
        """ctag :                             complex_tense_modal
ctag :                             complex_tense_modal
{$$ = new_node_1(CTAG,$1);}
     | ctag joik_opt_kebo free_seq complex_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | ctag joik_opt_kebo          complex_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
     | ctag jek_opt_kebo  free_seq complex_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | ctag jek_opt_kebo           complex_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
     | ctag joik_opt_kebo free_seq simple_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | ctag joik_opt_kebo          simple_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
     | ctag jek_opt_kebo  free_seq simple_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | ctag jek_opt_kebo           simple_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
     | stag joik_opt_kebo free_seq complex_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | stag joik_opt_kebo          complex_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
     | stag jek_opt_kebo  free_seq complex_tense_modal
{$$ = new_node_4(CTAG,$1,$2,$3,$4);}
     | stag jek_opt_kebo           complex_tense_modal
{$$ = new_node_3(CTAG,$1,$2,$3);}
"""
        print "on_ctag: got %s %s %s %s" % (target, option, names, values)
        return

    def on_complex_tense_modal(self, target, option, names, values):
        """complex_tense_modal : FIhO free_seq selbri FEhU free_seq
complex_tense_modal : FIhO free_seq selbri FEhU free_seq
{$$ = new_node_5(COMPLEX_TENSE_MODAL,$1,$2,$3,$4,$5);}
                    | FIhO free_seq selbri FEhU
{$$ = new_node_4(COMPLEX_TENSE_MODAL,$1,$2,$3,$4);}
                    | FIhO          selbri FEhU free_seq
{$$ = new_node_4(COMPLEX_TENSE_MODAL,$1,$2,$3,$4);}
                    | FIhO          selbri FEhU
{$$ = new_node_3(COMPLEX_TENSE_MODAL,$1,$2,$3);}
                    | simple_tense_modal free_seq
{$$ = new_node_2(COMPLEX_TENSE_MODAL,$1,$2);}
"""
        print "on_complex_tense_modal: got %s %s %s %s" % (target, option, names, values)
        return

    def on_stag(self, target, option, names, values):
        """stag :                    simple_tense_modal
stag :                    simple_tense_modal
{$$ = new_node_1(STAG,$1);}
     | stag jek_opt_kebo  simple_tense_modal
{$$ = new_node_3(STAG,$1,$2,$3);}
     | stag joik_opt_kebo simple_tense_modal
{$$ = new_node_3(STAG,$1,$2,$3);}
"""
        print "on_stag: got %s %s %s %s" % (target, option, names, values)
        return

    def on_simple_tense_modal(self, target, option, names, values):
        """simple_tense_modal : PRIVATE_START_TENSE NAhE se_bai  NAI KI PRIVATE_END_TENSE
simple_tense_modal : PRIVATE_START_TENSE NAhE se_bai  NAI KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE se_bai  NAI    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE se_bai      KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE se_bai         PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE NAhE    bai1 NAI KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE    bai1 NAI    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE    bai1     KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE    bai1        PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      se_bai  NAI KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      se_bai  NAI    PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      se_bai      KI PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      se_bai         PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE         bai1 NAI KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE         bai1 NAI    PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE         bai1     KI PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE         bai1        PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE NAhE time  space CAhA KI PRIVATE_END_TENSE
{$$ = new_node_5(SIMPLE_TENSE_MODAL,$2,$3,$4,$5,$6);}
                   | PRIVATE_START_TENSE NAhE time  space CAhA    PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE time  space      KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE time  space         PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE time        CAhA KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE time        CAhA    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE time             KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE time                PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      time  space CAhA KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE      time  space CAhA    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      time  space      KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      time  space         PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      time        CAhA KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      time        CAhA    PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      time             KI PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      time                PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE NAhE space time  CAhA KI PRIVATE_END_TENSE
{$$ = new_node_5(SIMPLE_TENSE_MODAL,$2,$3,$4,$5,$6);}
                   | PRIVATE_START_TENSE NAhE space time  CAhA    PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE space time       KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE space time          PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE space       CAhA KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE NAhE space       CAhA    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE space            KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE space               PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      space time  CAhA KI PRIVATE_END_TENSE
{$$ = new_node_4(SIMPLE_TENSE_MODAL,$2,$3,$4,$5);}
                   | PRIVATE_START_TENSE      space time  CAhA    PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      space time       KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      space time          PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      space       CAhA KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE      space       CAhA    PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      space            KI PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE      space               PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE                  CAhA KI PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE                  CAhA    PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE NAhE             CAhA KI PRIVATE_END_TENSE
{$$ = new_node_3(SIMPLE_TENSE_MODAL,$2,$3,$4);}
                   | PRIVATE_START_TENSE NAhE             CAhA    PRIVATE_END_TENSE
{$$ = new_node_2(SIMPLE_TENSE_MODAL,$2,$3);}
                   | PRIVATE_START_TENSE KI   PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
                   | PRIVATE_START_TENSE CUhE PRIVATE_END_TENSE
{$$ = new_node_1(SIMPLE_TENSE_MODAL,$2);}
"""
        print "on_simple_tense_modal: got %s %s %s %s" % (target, option, names, values)
        return

    def on_se_bai(self, target, option, names, values):
        """se_bai : SE BAI
se_bai : SE BAI
{$$ = new_node_2(SE_BAI,$1,$2);}
"""
        print "on_se_bai: got %s %s %s %s" % (target, option, names, values)
        return

    def on_bai1(self, target, option, names, values):
        """bai1 : BAI
bai1 : BAI
{$$ = new_node_1(BAI1,$1);}
"""
        print "on_bai1: got %s %s %s %s" % (target, option, names, values)
        return

    def on_time(self, target, option, names, values):
        """time : ZI time_offset_seq zeha_pu_nai interval_property_seq
time : ZI time_offset_seq zeha_pu_nai interval_property_seq
{$$ = new_node_4(TIME,$1,$2,$3,$4);}
     | ZI time_offset_seq             interval_property_seq
{$$ = new_node_3(TIME,$1,$2,$3);}
     | ZI time_offset_seq zeha_pu_nai
{$$ = new_node_3(TIME,$1,$2,$3);}
     | ZI time_offset_seq
{$$ = new_node_2(TIME,$1,$2);}
     | ZI                 zeha_pu_nai interval_property_seq
{$$ = new_node_3(TIME,$1,$2,$3);}
     | ZI                             interval_property_seq
{$$ = new_node_2(TIME,$1,$2);}
     | ZI                 zeha_pu_nai
{$$ = new_node_2(TIME,$1,$2);}
     | ZI                
{$$ = new_node_1(TIME,$1);}
     |    time_offset_seq zeha_pu_nai interval_property_seq
{$$ = new_node_3(TIME,$1,$2,$3);}
     |    time_offset_seq             interval_property_seq
{$$ = new_node_2(TIME,$1,$2);}
     |    time_offset_seq zeha_pu_nai
{$$ = new_node_2(TIME,$1,$2);}
     |    time_offset_seq
{$$ = new_node_1(TIME,$1);}
     |                    zeha_pu_nai interval_property_seq
{$$ = new_node_2(TIME,$1,$2);}
     |                                interval_property_seq
{$$ = new_node_1(TIME,$1);}
     |                    zeha_pu_nai
{$$ = new_node_1(TIME,$1);}
"""
        print "on_time: got %s %s %s %s" % (target, option, names, values)
        return

    def on_zeha_pu_nai(self, target, option, names, values):
        """zeha_pu_nai : ZEhA PU NAI
zeha_pu_nai : ZEhA PU NAI
{$$ = new_node_3(ZEHA_PU_NAI,$1,$2,$3);}
            | ZEhA PU
{$$ = new_node_2(ZEHA_PU_NAI,$1,$2);}
            | ZEhA
{$$ = new_node_1(ZEHA_PU_NAI,$1);}
"""
        print "on_zeha_pu_nai: got %s %s %s %s" % (target, option, names, values)
        return

    def on_time_offset(self, target, option, names, values):
        """time_offset : PU NAI ZI
time_offset : PU NAI ZI
{$$ = new_node_3(TIME_OFFSET,$1,$2,$3);}
            | PU NAI
{$$ = new_node_2(TIME_OFFSET,$1,$2);}
            | PU     ZI
{$$ = new_node_2(TIME_OFFSET,$1,$2);}
            | PU
{$$ = new_node_1(TIME_OFFSET,$1);}
"""
        print "on_time_offset: got %s %s %s %s" % (target, option, names, values)
        return

    def on_time_offset_seq(self, target, option, names, values):
        """time_offset_seq : time_offset_seq time_offset
time_offset_seq : time_offset_seq time_offset
{$$ = new_node_2(TIME_OFFSET_SEQ,$1,$2);}
                |                 time_offset
{$$ = new_node_1(TIME_OFFSET_SEQ,$1);}
"""
        print "on_time_offset_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space(self, target, option, names, values):
        """space : VA space_offset_seq space_interval MOhI space_offset
space : VA space_offset_seq space_interval MOhI space_offset
{$$ = new_node_5(SPACE,$1,$2,$3,$4,$5);}
      | VA space_offset_seq space_interval
{$$ = new_node_3(SPACE,$1,$2,$3);}
      | VA space_offset_seq                MOhI space_offset
{$$ = new_node_4(SPACE,$1,$2,$3,$4);}
      | VA space_offset_seq
{$$ = new_node_2(SPACE,$1,$2);}
      | VA                  space_interval MOhI space_offset
{$$ = new_node_4(SPACE,$1,$2,$3,$4);}
      | VA                  space_interval
{$$ = new_node_2(SPACE,$1,$2);}
      | VA                                 MOhI space_offset
{$$ = new_node_3(SPACE,$1,$2,$3);}
      | VA                 
{$$ = new_node_1(SPACE,$1);}
      |    space_offset_seq space_interval MOhI space_offset
{$$ = new_node_4(SPACE,$1,$2,$3,$4);}
      |    space_offset_seq space_interval
{$$ = new_node_2(SPACE,$1,$2);}
      |    space_offset_seq                MOhI space_offset
{$$ = new_node_3(SPACE,$1,$2,$3);}
      |    space_offset_seq
{$$ = new_node_1(SPACE,$1);}
      |                     space_interval MOhI space_offset
{$$ = new_node_3(SPACE,$1,$2,$3);}
      |                     space_interval
{$$ = new_node_1(SPACE,$1);}
      |                                    MOhI space_offset
{$$ = new_node_2(SPACE,$1,$2);}
"""
        print "on_space: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space_offset(self, target, option, names, values):
        """space_offset : FAhA NAI VA
space_offset : FAhA NAI VA
{$$ = new_node_3(SPACE_OFFSET,$1,$2,$3);}
             | FAhA NAI
{$$ = new_node_2(SPACE_OFFSET,$1,$2);}
             | FAhA     VA
{$$ = new_node_2(SPACE_OFFSET,$1,$2);}
             | FAhA
{$$ = new_node_1(SPACE_OFFSET,$1);}
"""
        print "on_space_offset: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space_offset_seq(self, target, option, names, values):
        """space_offset_seq : space_offset_seq space_offset
space_offset_seq : space_offset_seq space_offset
{$$ = new_node_2(SPACE_OFFSET_SEQ,$1,$2);}
                 |                  space_offset
{$$ = new_node_1(SPACE_OFFSET_SEQ,$1);}
"""
        print "on_space_offset_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space_interval(self, target, option, names, values):
        """space_interval : VEhA VIhA FAhA NAI space_int_props
space_interval : VEhA VIhA FAhA NAI space_int_props
{$$ = new_node_5(SPACE_INTERVAL,$1,$2,$3,$4,$5);}
               | VEhA VIhA FAhA     space_int_props
{$$ = new_node_4(SPACE_INTERVAL,$1,$2,$3,$4);}
               | VEhA VIhA          space_int_props
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               | VEhA      FAhA NAI space_int_props
{$$ = new_node_4(SPACE_INTERVAL,$1,$2,$3,$4);}
               | VEhA      FAhA     space_int_props
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               | VEhA               space_int_props
{$$ = new_node_2(SPACE_INTERVAL,$1,$2);}
               |      VIhA FAhA NAI space_int_props
{$$ = new_node_4(SPACE_INTERVAL,$1,$2,$3,$4);}
               |      VIhA FAhA     space_int_props
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               |      VIhA          space_int_props
{$$ = new_node_2(SPACE_INTERVAL,$1,$2);}
               | VEhA VIhA FAhA NAI
{$$ = new_node_4(SPACE_INTERVAL,$1,$2,$3,$4);}
               | VEhA VIhA FAhA
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               | VEhA VIhA
{$$ = new_node_2(SPACE_INTERVAL,$1,$2);}
               | VEhA      FAhA NAI
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               | VEhA      FAhA
{$$ = new_node_2(SPACE_INTERVAL,$1,$2);}
               | VEhA
{$$ = new_node_1(SPACE_INTERVAL,$1);}
               |      VIhA FAhA NAI
{$$ = new_node_3(SPACE_INTERVAL,$1,$2,$3);}
               |      VIhA FAhA
{$$ = new_node_2(SPACE_INTERVAL,$1,$2);}
               |      VIhA
{$$ = new_node_1(SPACE_INTERVAL,$1);}
               |                    space_int_props
{$$ = new_node_1(SPACE_INTERVAL,$1);}
"""
        print "on_space_interval: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space_int_props(self, target, option, names, values):
        """space_int_props : space_int_props space_int_prop
space_int_props : space_int_props space_int_prop
{$$ = new_node_2(SPACE_INT_PROPS,$1,$2);}
                |                 space_int_prop
{$$ = new_node_1(SPACE_INT_PROPS,$1);}
"""
        print "on_space_int_props: got %s %s %s %s" % (target, option, names, values)
        return

    def on_space_int_prop(self, target, option, names, values):
        """space_int_prop : FEhE interval_property
space_int_prop : FEhE interval_property
{$$ = new_node_2(SPACE_INT_PROP,$1,$2);}
"""
        print "on_space_int_prop: got %s %s %s %s" % (target, option, names, values)
        return

    def on_interval_property(self, target, option, names, values):
        """interval_property : PRIVATE_NUMBER_ROI number ROI NAI
interval_property : PRIVATE_NUMBER_ROI number ROI NAI
{$$ = new_node_3(INTERVAL_PROPERTY,$2,$3,$4);}
                  | PRIVATE_NUMBER_ROI number ROI
{$$ = new_node_2(INTERVAL_PROPERTY,$2,$3);}
                  | TAhE NAI
{$$ = new_node_2(INTERVAL_PROPERTY,$1,$2);}
                  | TAhE
{$$ = new_node_1(INTERVAL_PROPERTY,$1);}
                  | ZAhO NAI
{$$ = new_node_2(INTERVAL_PROPERTY,$1,$2);}
                  | ZAhO
{$$ = new_node_1(INTERVAL_PROPERTY,$1);}
"""
        print "on_interval_property: got %s %s %s %s" % (target, option, names, values)
        return

    def on_interval_property_seq(self, target, option, names, values):
        """interval_property_seq : interval_property_seq interval_property
interval_property_seq : interval_property_seq interval_property
{$$ = new_node_2(INTERVAL_PROPERTY_SEQ,$1,$2);}
                      |                       interval_property
{$$ = new_node_1(INTERVAL_PROPERTY_SEQ,$1);}
"""
        print "on_interval_property_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_free_seq(self, target, option, names, values):
        """free_seq : free_seq free
free_seq : free_seq free
{$$ = new_node_2(FREE_SEQ,$1,$2);}
         |          free
{$$ = new_node_1(FREE_SEQ,$1);}
"""
        print "on_free_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_free(self, target, option, names, values):
        """free : metalinguistic
free : metalinguistic
{$$ = new_node_1(FREE,$1);}
     | reciprocity
{$$ = new_node_1(FREE,$1);}
     | free_vocative
{$$ = new_node_1(FREE,$1);}
     | utterance_ordinal
{$$ = new_node_1(FREE,$1);}
     | parenthetical
{$$ = new_node_1(FREE,$1);}
     | subscript
{$$ = new_node_1(FREE,$1);}
"""
        print "on_free: got %s %s %s %s" % (target, option, names, values)
        return

    def on_metalinguistic(self, target, option, names, values):
        """metalinguistic : SEI free_seq terms CU free_seq metalinguistic_main_selbri SEhU
metalinguistic : SEI free_seq terms CU free_seq metalinguistic_main_selbri SEhU
{$$ = new_node_7(METALINGUISTIC,$1,$2,$3,$4,$5,$6,$7);}
               | SEI free_seq terms CU          metalinguistic_main_selbri SEhU
{$$ = new_node_6(METALINGUISTIC,$1,$2,$3,$4,$5,$6);}
               | SEI free_seq terms             metalinguistic_main_selbri SEhU
{$$ = new_node_5(METALINGUISTIC,$1,$2,$3,$4,$5);}
               | SEI free_seq                   metalinguistic_main_selbri SEhU
{$$ = new_node_4(METALINGUISTIC,$1,$2,$3,$4);}
               | SEI          terms CU free_seq metalinguistic_main_selbri SEhU
{$$ = new_node_6(METALINGUISTIC,$1,$2,$3,$4,$5,$6);}
               | SEI          terms CU          metalinguistic_main_selbri SEhU
{$$ = new_node_5(METALINGUISTIC,$1,$2,$3,$4,$5);}
               | SEI          terms             metalinguistic_main_selbri SEhU
{$$ = new_node_4(METALINGUISTIC,$1,$2,$3,$4);}
               | SEI                            metalinguistic_main_selbri SEhU
{$$ = new_node_3(METALINGUISTIC,$1,$2,$3);}
"""
        print "on_metalinguistic: got %s %s %s %s" % (target, option, names, values)
        return

    def on_metalinguistic_main_selbri(self, target, option, names, values):
        """metalinguistic_main_selbri : selbri
metalinguistic_main_selbri : selbri
{$$ = new_node_1(METALINGUISTIC_MAIN_SELBRI,$1);}
"""
        print "on_metalinguistic_main_selbri: got %s %s %s %s" % (target, option, names, values)
        return

    def on_reciprocity(self, target, option, names, values):
        """reciprocity : SOI free_seq sumti sumti SEhU
reciprocity : SOI free_seq sumti sumti SEhU
{$$ = new_node_5(RECIPROCITY,$1,$2,$3,$4,$5);}
            | SOI free_seq sumti       SEhU
{$$ = new_node_4(RECIPROCITY,$1,$2,$3,$4);}
            | SOI          sumti sumti SEhU
{$$ = new_node_4(RECIPROCITY,$1,$2,$3,$4);}
            | SOI          sumti       SEhU
{$$ = new_node_3(RECIPROCITY,$1,$2,$3);}
"""
        print "on_reciprocity: got %s %s %s %s" % (target, option, names, values)
        return

    def on_free_vocative(self, target, option, names, values):
        """free_vocative : vocative relative_clauses selbri relative_clauses DOhU
free_vocative : vocative relative_clauses selbri relative_clauses DOhU
{$$ = new_node_5(FREE_VOCATIVE,$1,$2,$3,$4,$5);}
              | vocative relative_clauses selbri                  DOhU
{$$ = new_node_4(FREE_VOCATIVE,$1,$2,$3,$4);}
              | vocative                  selbri relative_clauses DOhU
{$$ = new_node_4(FREE_VOCATIVE,$1,$2,$3,$4);}
              | vocative                  selbri                  DOhU
{$$ = new_node_3(FREE_VOCATIVE,$1,$2,$3);}
              | vocative relative_clauses CMENE_seq free_seq relative_clauses DOhU
{$$ = new_node_6(FREE_VOCATIVE,$1,$2,$3,$4,$5,$6);}
              | vocative relative_clauses CMENE_seq free_seq                  DOhU
{$$ = new_node_5(FREE_VOCATIVE,$1,$2,$3,$4,$5);}
              | vocative                  CMENE_seq free_seq relative_clauses DOhU
{$$ = new_node_5(FREE_VOCATIVE,$1,$2,$3,$4,$5);}
              | vocative                  CMENE_seq free_seq                  DOhU
{$$ = new_node_4(FREE_VOCATIVE,$1,$2,$3,$4);}
              | vocative relative_clauses CMENE_seq          relative_clauses DOhU
{$$ = new_node_5(FREE_VOCATIVE,$1,$2,$3,$4,$5);}
              | vocative relative_clauses CMENE_seq                           DOhU
{$$ = new_node_4(FREE_VOCATIVE,$1,$2,$3,$4);}
              | vocative                  CMENE_seq          relative_clauses DOhU
{$$ = new_node_4(FREE_VOCATIVE,$1,$2,$3,$4);}
              | vocative                  CMENE_seq                           DOhU
{$$ = new_node_3(FREE_VOCATIVE,$1,$2,$3);}
              | vocative sumti DOhU
{$$ = new_node_3(FREE_VOCATIVE,$1,$2,$3);}
              | vocative       DOhU
{$$ = new_node_2(FREE_VOCATIVE,$1,$2);}
"""
        print "on_free_vocative: got %s %s %s %s" % (target, option, names, values)
        return

    def on_utterance_ordinal(self, target, option, names, values):
        """utterance_ordinal : PRIVATE_NUMBER_MAI number       MAI
utterance_ordinal : PRIVATE_NUMBER_MAI number       MAI
{$$ = new_node_2(UTTERANCE_ORDINAL,$2,$3);}
                  | PRIVATE_NUMBER_MAI lerfu_string MAI
{$$ = new_node_2(UTTERANCE_ORDINAL,$2,$3);}
"""
        print "on_utterance_ordinal: got %s %s %s %s" % (target, option, names, values)
        return

    def on_parenthetical(self, target, option, names, values):
        """parenthetical : TO text TOI
parenthetical : TO text TOI
{$$ = new_node_3(PARENTHETICAL,$1,$2,$3);}
"""
        print "on_parenthetical: got %s %s %s %s" % (target, option, names, values)
        return

    def on_subscript(self, target, option, names, values):
        """subscript : XI free_seq number       BOI
subscript : XI free_seq number       BOI
{$$ = new_node_4(SUBSCRIPT,$1,$2,$3,$4);}
          | XI          number       BOI
{$$ = new_node_3(SUBSCRIPT,$1,$2,$3);}
          | XI free_seq lerfu_string BOI
{$$ = new_node_4(SUBSCRIPT,$1,$2,$3,$4);}
          | XI          lerfu_string BOI
{$$ = new_node_3(SUBSCRIPT,$1,$2,$3);}
          | XI free_seq VEI free_seq mex VEhO
{$$ = new_node_6(SUBSCRIPT,$1,$2,$3,$4,$5,$6);}
          | XI free_seq VEI          mex VEhO
{$$ = new_node_5(SUBSCRIPT,$1,$2,$3,$4,$5);}
          | XI          VEI free_seq mex VEhO
{$$ = new_node_5(SUBSCRIPT,$1,$2,$3,$4,$5);}
          | XI          VEI          mex VEhO
{$$ = new_node_4(SUBSCRIPT,$1,$2,$3,$4);}
"""
        print "on_subscript: got %s %s %s %s" % (target, option, names, values)
        return

    def on_vocative(self, target, option, names, values):
        """vocative : coi_nai_seq DOI
vocative : coi_nai_seq DOI
{$$ = new_node_2(VOCATIVE,$1,$2);}
         | coi_nai_seq
{$$ = new_node_1(VOCATIVE,$1);}
         |             DOI
{$$ = new_node_1(VOCATIVE,$1);}
"""
        print "on_vocative: got %s %s %s %s" % (target, option, names, values)
        return

    def on_coi_nai_seq(self, target, option, names, values):
        """coi_nai_seq : COI NAI
coi_nai_seq : COI NAI
{$$ = new_node_2(COI_NAI_SEQ,$1,$2);}
            | COI
{$$ = new_node_1(COI_NAI_SEQ,$1);}
            | coi_nai_seq COI NAI
{$$ = new_node_3(COI_NAI_SEQ,$1,$2,$3);}
            | coi_nai_seq COI
{$$ = new_node_2(COI_NAI_SEQ,$1,$2);}
"""
        print "on_coi_nai_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_indicators(self, target, option, names, values):
        """indicators : FUhE indicator_seq
indicators : FUhE indicator_seq
{$$ = new_node_2(INDICATORS,$1,$2);}
           |      indicator_seq
{$$ = new_node_1(INDICATORS,$1);}
"""
        print "on_indicators: got %s %s %s %s" % (target, option, names, values)
        return

    def on_indicator_seq(self, target, option, names, values):
        """indicator_seq : indicator_seq indicator
indicator_seq : indicator_seq indicator
{$$ = new_node_2(INDICATOR_SEQ,$1,$2);}
              |               indicator
{$$ = new_node_1(INDICATOR_SEQ,$1);}
"""
        print "on_indicator_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_indicator(self, target, option, names, values):
        """indicator : UI  NAI
indicator : UI  NAI
{$$ = new_node_2(INDICATOR,$1,$2);}
          | UI
{$$ = new_node_1(INDICATOR,$1);}
          | CAI NAI
{$$ = new_node_2(INDICATOR,$1,$2);}
          | CAI
{$$ = new_node_1(INDICATOR,$1);}
          | Y
{$$ = new_node_1(INDICATOR,$1);}
          | DAhO
{$$ = new_node_1(INDICATOR,$1);}
          | FUhO
{$$ = new_node_1(INDICATOR,$1);}
"""
        print "on_indicator: got %s %s %s %s" % (target, option, names, values)
        return

    def on_NAI_seq(self, target, option, names, values):
        """NAI_seq : NAI_seq NAI
NAI_seq : NAI_seq NAI
{$$ = new_node_2(NAI_SEQ,$1,$2);}
        |         NAI
{$$ = new_node_1(NAI_SEQ,$1);}
"""
        print "on_NAI_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_CMENE_seq(self, target, option, names, values):
        """CMENE_seq : CMENE_seq CMENE
CMENE_seq : CMENE_seq CMENE
{$$ = new_node_2(CMENE_SEQ,$1,$2);}
          |           CMENE
{$$ = new_node_1(CMENE_SEQ,$1);}
"""
        print "on_CMENE_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_NIhO_seq_free_seq(self, target, option, names, values):
        """NIhO_seq_free_seq : NIhO_seq free_seq
NIhO_seq_free_seq : NIhO_seq free_seq
{$$ = new_node_2(NIHO_SEQ_FREE_SEQ,$1,$2);}
                  | NIhO_seq
{$$ = new_node_1(NIHO_SEQ_FREE_SEQ,$1);}
"""
        print "on_NIhO_seq_free_seq: got %s %s %s %s" % (target, option, names, values)
        return

    def on_NIhO_seq(self, target, option, names, values):
        """NIhO_seq : NIhO_seq NIhO
NIhO_seq : NIhO_seq NIhO
{$$ = new_node_2(NIHO_SEQ,$1,$2);}
         |          NIhO
{$$ = new_node_1(NIHO_SEQ,$1);}
"""
        print "on_NIhO_seq: got %s %s %s %s" % (target, option, names, values)
        return

p = Parser()
