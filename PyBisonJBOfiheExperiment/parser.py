#!/usr/bin/env python

"""
PyBison file automatically generated from grammar file uncomm.y
You can edit this module, or import it and subclass the Parser class
"""

import sys

from bison import BisonParser, BisonNode, BisonError

bisonFile = "uncomm.y"  # original bison file
lexFile = "cm_scan.l"    # original flex file

class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "uncomm.y" and lex file "cm_scan.l"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """

    # -------------------------------------------------
    # Default class to use for creating new parse nodes
    # -------------------------------------------------
    defaultNodeClass = BisonNode

    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = "parser-engine"

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = ['GARBAGE', 'A', 'BAhE', 'BAI', 'BE', 'BEhO', 'BEI', 'BIhE', 'BIhI', 'BO', 'BOI', 'BRIVLA', 'BU', 'BY', 'CAhA', 'CAI', 'CEhE', 'CEI', 'CMENE', 'CO', 'COI', 'CU', 'CUhE', 'DAhO', 'DOhU', 'DOI', 'FA', 'FAhA', 'FAhO', 'FEhE', 'FEhU', 'FIhO', 'FOI', 'FUhA', 'FUhE', 'FUhO', 'GA', 'GAhO', 'GEhU', 'GI', 'GIhA', 'GOhA', 'GOI', 'GUhA', 'I', 'JA', 'JAI', 'JOhI', 'JOI', 'KE', 'KEhE', 'KEI', 'KI', 'KOhA', 'KUhE', 'KUhO', 'KU', 'LA', 'LAhE', 'LAU', 'LE', 'LEhU', 'LI', 'LIhU', 'LOhO', 'LOhU', 'LU', 'LUhU', 'MAhO', 'MAI', 'ME', 'MEhU', 'MOhE', 'MOhI', 'MOI', 'NA', 'NAhE', 'NAhU', 'NAI', 'NIhE', 'NIhO', 'NOI', 'NU', 'NUhA', 'NUhI', 'NUhU', 'PA', 'PEhA', 'PEhE', 'PEhO', 'POhA', 'PU', 'RAhO', 'ROI', 'SA', 'SE', 'SEhU', 'SEI', 'SI', 'SOI', 'SU', 'TAhE', 'TEhU', 'TEI', 'TO', 'TOI', 'TUhE', 'TUhU', 'UI', 'VA', 'VAU', 'VEhA', 'VEhO', 'VEI', 'VIhA', 'VUhO', 'VUhU', 'XI', 'Y', 'ZAhO', 'ZEhA', 'ZEI', 'ZI', 'ZIhE', 'ZO', 'ZOhU', 'ZOI', 'PRIVATE_START_EK', 'PRIVATE_START_GIHEK', 'PRIVATE_START_GUHEK', 'PRIVATE_START_JEK', 'PRIVATE_END_JEK', 'PRIVATE_START_JOIK', 'PRIVATE_END_JOIK', 'PRIVATE_START_GEK', 'PRIVATE_START_BAI', 'PRIVATE_EK_KE', 'PRIVATE_EK_BO', 'PRIVATE_JEK_KE', 'PRIVATE_JEK_BO', 'PRIVATE_JOIK_KE', 'PRIVATE_JOIK_BO', 'PRIVATE_I_JEKJOIK', 'PRIVATE_I_BO', 'PRIVATE_GIHEK_KE', 'PRIVATE_GIHEK_BO', 'PRIVATE_NAhE_BO', 'PRIVATE_NAhE_time', 'PRIVATE_NAhE_space', 'PRIVATE_NAhE_CAhA', 'PRIVATE_NA_KU', 'PRIVATE_NUMBER_MAI', 'PRIVATE_NUMBER_MOI', 'PRIVATE_NUMBER_ROI', 'PRIVATE_START_TENSE', 'PRIVATE_END_TENSE', 'PRIVATE_EOF_MARK', 'IMPOSSIBLE_TOKEN']

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        )

    # ---------------------------------------------------------------
    # Declare the start target here (by name)
    # ---------------------------------------------------------------
    start = "all"

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    def on_all(self, target, option, names, values):
        """
        all
            : text
        """
        return self.defaultNodeClass(
            target="all",
            option=option,
            names=names,
            values=values)

    def on_text(self, target, option, names, values):
        """
        text
            : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq text_1
            | NAI_seq CMENE_seq free_seq jek_opt_ke free_seq text_1
            | NAI_seq CMENE_seq free_seq joik_opt_ke text_1
            | NAI_seq CMENE_seq free_seq jek_opt_ke text_1
            | NAI_seq CMENE_seq free_seq text_1
            | NAI_seq CMENE_seq joik_opt_ke free_seq text_1
            | NAI_seq CMENE_seq jek_opt_ke free_seq text_1
            | NAI_seq CMENE_seq joik_opt_ke text_1
            | NAI_seq CMENE_seq jek_opt_ke text_1
            | NAI_seq CMENE_seq text_1
            | NAI_seq indicators free_seq joik_opt_ke free_seq text_1
            | NAI_seq indicators free_seq jek_opt_ke free_seq text_1
            | NAI_seq indicators free_seq joik_opt_ke text_1
            | NAI_seq indicators free_seq jek_opt_ke text_1
            | NAI_seq indicators free_seq text_1
            | NAI_seq indicators joik_opt_ke free_seq text_1
            | NAI_seq indicators jek_opt_ke free_seq text_1
            | NAI_seq indicators joik_opt_ke text_1
            | NAI_seq indicators jek_opt_ke text_1
            | NAI_seq indicators text_1
            | NAI_seq free_seq joik_opt_ke free_seq text_1
            | NAI_seq free_seq jek_opt_ke free_seq text_1
            | NAI_seq free_seq joik_opt_ke text_1
            | NAI_seq free_seq jek_opt_ke text_1
            | NAI_seq free_seq text_1
            | NAI_seq joik_opt_ke free_seq text_1
            | NAI_seq jek_opt_ke free_seq text_1
            | NAI_seq joik_opt_ke text_1
            | NAI_seq jek_opt_ke text_1
            | NAI_seq text_1
            | CMENE_seq free_seq joik_opt_ke free_seq text_1
            | CMENE_seq free_seq jek_opt_ke free_seq text_1
            | CMENE_seq free_seq joik_opt_ke text_1
            | CMENE_seq free_seq jek_opt_ke text_1
            | CMENE_seq free_seq text_1
            | CMENE_seq joik_opt_ke free_seq text_1
            | CMENE_seq jek_opt_ke free_seq text_1
            | CMENE_seq joik_opt_ke text_1
            | CMENE_seq jek_opt_ke text_1
            | CMENE_seq text_1
            | indicators free_seq joik_opt_ke free_seq text_1
            | indicators free_seq jek_opt_ke free_seq text_1
            | indicators free_seq joik_opt_ke text_1
            | indicators free_seq jek_opt_ke text_1
            | indicators free_seq text_1
            | indicators joik_opt_ke free_seq text_1
            | indicators jek_opt_ke free_seq text_1
            | indicators joik_opt_ke text_1
            | indicators jek_opt_ke text_1
            | indicators text_1
            | free_seq joik_opt_ke free_seq text_1
            | free_seq jek_opt_ke free_seq text_1
            | free_seq joik_opt_ke text_1
            | free_seq jek_opt_ke text_1
            | free_seq text_1
            | joik_opt_ke free_seq text_1
            | jek_opt_ke free_seq text_1
            | joik_opt_ke text_1
            | jek_opt_ke text_1
            | text_1
        """
        return self.defaultNodeClass(
            target="text",
            option=option,
            names=names,
            values=values)

    def on_text_no_text_1(self, target, option, names, values):
        """
        text_no_text_1
            : NAI_seq CMENE_seq free_seq joik_opt_ke free_seq
            | NAI_seq CMENE_seq free_seq jek_opt_ke free_seq
            | NAI_seq CMENE_seq free_seq joik_opt_ke
            | NAI_seq CMENE_seq free_seq jek_opt_ke
            | NAI_seq CMENE_seq free_seq
            | NAI_seq CMENE_seq joik_opt_ke free_seq
            | NAI_seq CMENE_seq jek_opt_ke free_seq
            | NAI_seq CMENE_seq joik_opt_ke
            | NAI_seq CMENE_seq jek_opt_ke
            | NAI_seq CMENE_seq
            | NAI_seq indicators free_seq joik_opt_ke free_seq
            | NAI_seq indicators free_seq jek_opt_ke free_seq
            | NAI_seq indicators free_seq joik_opt_ke
            | NAI_seq indicators free_seq jek_opt_ke
            | NAI_seq indicators free_seq
            | NAI_seq indicators joik_opt_ke free_seq
            | NAI_seq indicators jek_opt_ke free_seq
            | NAI_seq indicators joik_opt_ke
            | NAI_seq indicators jek_opt_ke
            | NAI_seq indicators
            | NAI_seq free_seq joik_opt_ke free_seq
            | NAI_seq free_seq jek_opt_ke free_seq
            | NAI_seq free_seq joik_opt_ke
            | NAI_seq free_seq jek_opt_ke
            | NAI_seq free_seq
            | NAI_seq joik_opt_ke free_seq
            | NAI_seq jek_opt_ke free_seq
            | NAI_seq joik_opt_ke
            | NAI_seq jek_opt_ke
            | NAI_seq
            | CMENE_seq free_seq joik_opt_ke free_seq
            | CMENE_seq free_seq jek_opt_ke free_seq
            | CMENE_seq free_seq joik_opt_ke
            | CMENE_seq free_seq jek_opt_ke
            | CMENE_seq free_seq
            | CMENE_seq joik_opt_ke free_seq
            | CMENE_seq jek_opt_ke free_seq
            | CMENE_seq joik_opt_ke
            | CMENE_seq jek_opt_ke
            | CMENE_seq
            | indicators free_seq joik_opt_ke free_seq
            | indicators free_seq jek_opt_ke free_seq
            | indicators free_seq joik_opt_ke
            | indicators free_seq jek_opt_ke
            | indicators free_seq
            | indicators joik_opt_ke free_seq
            | indicators jek_opt_ke free_seq
            | indicators joik_opt_ke
            | indicators jek_opt_ke
            | indicators
            | free_seq joik_opt_ke free_seq
            | free_seq jek_opt_ke free_seq
            | free_seq joik_opt_ke
            | free_seq jek_opt_ke
            | free_seq
            | joik_opt_ke free_seq
            | jek_opt_ke free_seq
            | joik_opt_ke
            | jek_opt_ke
        """
        return self.defaultNodeClass(
            target="text_no_text_1",
            option=option,
            names=names,
            values=values)

    def on_text_1(self, target, option, names, values):
        """
        text_1
            : text_1A paragraphs
            | text_1A
            | paragraphs
            | /* Empty */
        """
        return self.defaultNodeClass(
            target="text_1",
            option=option,
            names=names,
            values=values)

    def on_text_1A(self, target, option, names, values):
        """
        text_1A
            : text_1B
            | NIhO_seq_free_seq
        """
        return self.defaultNodeClass(
            target="text_1A",
            option=option,
            names=names,
            values=values)

    def on_text_1B(self, target, option, names, values):
        """
        text_1B
            : text_1C
            | text_1B text_1C
        """
        return self.defaultNodeClass(
            target="text_1B",
            option=option,
            names=names,
            values=values)

    def on_text_1C(self, target, option, names, values):
        """
        text_1C
            : PRIVATE_I_BO I joik stag BO free_seq
            | PRIVATE_I_BO I jek stag BO free_seq
            | PRIVATE_I_BO I stag BO free_seq
            | PRIVATE_I_BO I joik stag BO
            | PRIVATE_I_BO I jek stag BO
            | PRIVATE_I_BO I stag BO
            | PRIVATE_I_BO I joik BO free_seq
            | PRIVATE_I_BO I jek BO free_seq
            | PRIVATE_I_BO I BO free_seq
            | PRIVATE_I_BO I joik BO
            | PRIVATE_I_BO I jek BO
            | PRIVATE_I_BO I BO
            | PRIVATE_I_JEKJOIK I joik_opt_ke free_seq
            | PRIVATE_I_JEKJOIK I jek_opt_ke free_seq
            | I free_seq
            | PRIVATE_I_JEKJOIK I joik_opt_ke
            | PRIVATE_I_JEKJOIK I jek_opt_ke
            | I
        """
        return self.defaultNodeClass(
            target="text_1C",
            option=option,
            names=names,
            values=values)

    def on_paragraphs(self, target, option, names, values):
        """
        paragraphs
            : paragraph
            | paragraphs NIhO_seq_free_seq paragraph
        """
        return self.defaultNodeClass(
            target="paragraphs",
            option=option,
            names=names,
            values=values)

    def on_paragraph(self, target, option, names, values):
        """
        paragraph
            : statement
            | fragment
            | paragraph i_opt_free_seq statement
            | paragraph i_opt_free_seq fragment
            | paragraph i_opt_free_seq
        """
        return self.defaultNodeClass(
            target="paragraph",
            option=option,
            names=names,
            values=values)

    def on_i_opt_free_seq(self, target, option, names, values):
        """
        i_opt_free_seq
            : I
            | I free_seq
        """
        return self.defaultNodeClass(
            target="i_opt_free_seq",
            option=option,
            names=names,
            values=values)

    def on_statement(self, target, option, names, values):
        """
        statement
            : inner_statement
        """
        return self.defaultNodeClass(
            target="statement",
            option=option,
            names=names,
            values=values)

    def on_inner_statement(self, target, option, names, values):
        """
        inner_statement
            : statement_1
            | prenex inner_statement
        """
        return self.defaultNodeClass(
            target="inner_statement",
            option=option,
            names=names,
            values=values)

    def on_statement_1(self, target, option, names, values):
        """
        statement_1
            : statement_2
            | statement_1 i_joik_jek statement_2
            | statement_1 i_joik_jek
        """
        return self.defaultNodeClass(
            target="statement_1",
            option=option,
            names=names,
            values=values)

    def on_i_joik_jek(self, target, option, names, values):
        """
        i_joik_jek
            : PRIVATE_I_JEKJOIK I joik_opt_ke free_seq
            | PRIVATE_I_JEKJOIK I joik_opt_ke
            | PRIVATE_I_JEKJOIK I jek_opt_ke free_seq
            | PRIVATE_I_JEKJOIK I jek_opt_ke
        """
        return self.defaultNodeClass(
            target="i_joik_jek",
            option=option,
            names=names,
            values=values)

    def on_statement_2(self, target, option, names, values):
        """
        statement_2
            : statement_3
            | statement_3 i_jj_stag_bo
            | statement_3 i_jj_stag_bo statement_2
        """
        return self.defaultNodeClass(
            target="statement_2",
            option=option,
            names=names,
            values=values)

    def on_i_jj_stag_bo(self, target, option, names, values):
        """
        i_jj_stag_bo
            : PRIVATE_I_BO I joik stag BO free_seq
            | PRIVATE_I_BO I joik stag BO
            | PRIVATE_I_BO I joik BO free_seq
            | PRIVATE_I_BO I joik BO
            | PRIVATE_I_BO I jek stag BO free_seq
            | PRIVATE_I_BO I jek stag BO
            | PRIVATE_I_BO I jek BO free_seq
            | PRIVATE_I_BO I jek BO
            | PRIVATE_I_BO I stag BO free_seq
            | PRIVATE_I_BO I stag BO
            | PRIVATE_I_BO I BO free_seq
            | PRIVATE_I_BO I BO
        """
        return self.defaultNodeClass(
            target="i_jj_stag_bo",
            option=option,
            names=names,
            values=values)

    def on_statement_3(self, target, option, names, values):
        """
        statement_3
            : sentence
            | tag TUhE free_seq text_1 TUhU free_seq
            | tag TUhE free_seq text_1 TUhU
            | tag TUhE free_seq text_1 /* ET TUhU */
            | tag TUhE text_1 TUhU free_seq
            | tag TUhE text_1 TUhU
            | tag TUhE text_1 /* ET TUhU */
            | TUhE free_seq text_1 TUhU free_seq
            | TUhE free_seq text_1 TUhU
            | TUhE free_seq text_1 /* ET TUhU */
            | TUhE text_1 TUhU free_seq
            | TUhE text_1 TUhU
            | TUhE text_1 /* ET TUhU */
        """
        return self.defaultNodeClass(
            target="statement_3",
            option=option,
            names=names,
            values=values)

    def on_fragment(self, target, option, names, values):
        """
        fragment
            : ek free_seq
            | ek
            | gihek free_seq
            | gihek
            | quantifier
            | NA free_seq
            | NA
            | terms VAU free_seq
            | terms VAU
            | terms /* ET VAU */
            | prenex
            | relative_clauses
            | links
            | linkargs
        """
        return self.defaultNodeClass(
            target="fragment",
            option=option,
            names=names,
            values=values)

    def on_prenex(self, target, option, names, values):
        """
        prenex
            : terms ZOhU free_seq
            | terms ZOhU
        """
        return self.defaultNodeClass(
            target="prenex",
            option=option,
            names=names,
            values=values)

    def on_sentence(self, target, option, names, values):
        """
        sentence
            : terms CU free_seq bridi_tail
            | terms CU bridi_tail
            | no_cu_sentence
            | observative_sentence
            | terms PRIVATE_START_GIHEK /* error */
            | terms PRIVATE_GIHEK_KE /* error */
            | terms PRIVATE_GIHEK_BO /* error */
        """
        return self.defaultNodeClass(
            target="sentence",
            option=option,
            names=names,
            values=values)

    def on_no_cu_sentence(self, target, option, names, values):
        """
        no_cu_sentence
            : IMPOSSIBLE_TOKEN
            | terms /* ET CU */ bridi_tail
        """
        return self.defaultNodeClass(
            target="no_cu_sentence",
            option=option,
            names=names,
            values=values)

    def on_observative_sentence(self, target, option, names, values):
        """
        observative_sentence
            : bridi_tail
        """
        return self.defaultNodeClass(
            target="observative_sentence",
            option=option,
            names=names,
            values=values)

    def on_subsentence(self, target, option, names, values):
        """
        subsentence
            : sentence
            | prenex subsentence
        """
        return self.defaultNodeClass(
            target="subsentence",
            option=option,
            names=names,
            values=values)

    def on_bridi_tail(self, target, option, names, values):
        """
        bridi_tail
            : bridi_tail_1
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE free_seq tail_terms
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE free_seq /* ET VAU */
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE tail_terms
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail KEhE /* ET VAU */
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail /* ET KEhE */ tail_terms
            | bridi_tail_1 gihek_stag_ke KE free_seq bridi_tail /* ET KEhE */ /* ET VAU */
            | bridi_tail_1 gihek_stag_ke KE bridi_tail KEhE free_seq tail_terms
            | bridi_tail_1 gihek_stag_ke KE bridi_tail KEhE free_seq /* ET VAU */
            | bridi_tail_1 gihek_stag_ke KE bridi_tail KEhE tail_terms
            | bridi_tail_1 gihek_stag_ke KE bridi_tail KEhE /* ET VAU */
            | bridi_tail_1 gihek_stag_ke KE bridi_tail /* ET KEhE */ tail_terms
            | bridi_tail_1 gihek_stag_ke KE bridi_tail /* ET VAU */
        """
        return self.defaultNodeClass(
            target="bridi_tail",
            option=option,
            names=names,
            values=values)

    def on_gihek_stag_ke(self, target, option, names, values):
        """
        gihek_stag_ke
            : PRIVATE_GIHEK_KE gihek stag
            | PRIVATE_GIHEK_KE gihek
        """
        return self.defaultNodeClass(
            target="gihek_stag_ke",
            option=option,
            names=names,
            values=values)

    def on_bridi_tail_1(self, target, option, names, values):
        """
        bridi_tail_1
            : bridi_tail_2
            | bridi_tail_1 gihek free_seq bridi_tail_2 tail_terms
            | bridi_tail_1 gihek free_seq bridi_tail_2 /* ET VAU */
            | bridi_tail_1 gihek bridi_tail_2 tail_terms
            | bridi_tail_1 gihek bridi_tail_2 /* ET VAU */
        """
        return self.defaultNodeClass(
            target="bridi_tail_1",
            option=option,
            names=names,
            values=values)

    def on_bridi_tail_2(self, target, option, names, values):
        """
        bridi_tail_2
            : bridi_tail_3
            | bridi_tail_2 gihek_stag_bo bridi_tail_2 tail_terms
            | bridi_tail_2 gihek_stag_bo bridi_tail_2 /* ET VAU */
        """
        return self.defaultNodeClass(
            target="bridi_tail_2",
            option=option,
            names=names,
            values=values)

    def on_gihek_stag_bo(self, target, option, names, values):
        """
        gihek_stag_bo
            : PRIVATE_GIHEK_BO gihek stag BO free_seq
            | PRIVATE_GIHEK_BO gihek stag BO
            | PRIVATE_GIHEK_BO gihek BO free_seq
            | PRIVATE_GIHEK_BO gihek BO
        """
        return self.defaultNodeClass(
            target="gihek_stag_bo",
            option=option,
            names=names,
            values=values)

    def on_bridi_tail_3(self, target, option, names, values):
        """
        bridi_tail_3
            : main_selbri tail_terms
            | main_selbri /* ET VAU */
            | gek_sentence
        """
        return self.defaultNodeClass(
            target="bridi_tail_3",
            option=option,
            names=names,
            values=values)

    def on_main_selbri(self, target, option, names, values):
        """
        main_selbri
            : selbri
        """
        return self.defaultNodeClass(
            target="main_selbri",
            option=option,
            names=names,
            values=values)

    def on_tail_terms(self, target, option, names, values):
        """
        tail_terms
            : terms VAU free_seq
            | terms VAU
            | terms /* ET VAU */
            | VAU free_seq
            | VAU
        """
        return self.defaultNodeClass(
            target="tail_terms",
            option=option,
            names=names,
            values=values)

    def on_gek_sentence(self, target, option, names, values):
        """
        gek_sentence
            : gek subsentence gik subsentence tail_terms
            | gek subsentence gik subsentence /* ET VAU */
            | tag KE free_seq gek_sentence KEhE free_seq
            | tag KE free_seq gek_sentence KEhE
            | tag KE free_seq gek_sentence /* ET KEhE */
            | tag KE gek_sentence KEhE free_seq
            | tag KE gek_sentence KEhE
            | tag KE gek_sentence /* ET KEhE */
            | KE free_seq gek_sentence KEhE free_seq
            | KE free_seq gek_sentence KEhE
            | KE free_seq gek_sentence /* ET KEhE */
            | KE gek_sentence KEhE free_seq
            | KE gek_sentence KEhE
            | KE gek_sentence /* ET KEhE */
            | NA free_seq gek_sentence
            | NA gek_sentence
        """
        return self.defaultNodeClass(
            target="gek_sentence",
            option=option,
            names=names,
            values=values)

    def on_terms(self, target, option, names, values):
        """
        terms
            : terms_1
            | terms terms_1
        """
        return self.defaultNodeClass(
            target="terms",
            option=option,
            names=names,
            values=values)

    def on_terms_1(self, target, option, names, values):
        """
        terms_1
            : terms_2
            | terms_1 PEhE free_seq joik free_seq terms_2
            | terms_1 PEhE free_seq joik terms_2
            | terms_1 PEhE free_seq jek free_seq terms_2
            | terms_1 PEhE free_seq jek terms_2
            | terms_1 PEhE joik free_seq terms_2
            | terms_1 PEhE joik terms_2
            | terms_1 PEhE jek free_seq terms_2
            | terms_1 PEhE jek terms_2
        """
        return self.defaultNodeClass(
            target="terms_1",
            option=option,
            names=names,
            values=values)

    def on_terms_2(self, target, option, names, values):
        """
        terms_2
            : term
            | terms_2 CEhE free_seq term
            | terms_2 CEhE term
        """
        return self.defaultNodeClass(
            target="terms_2",
            option=option,
            names=names,
            values=values)

    def on_term(self, target, option, names, values):
        """
        term
            : term_plain_sumti
            | term_tagged_sumti /* ET */
            | term_placed_sumti
            | term_floating_tense
            | termset
            | tagged_termset
            | term_floating_negate
            | term_other
        """
        return self.defaultNodeClass(
            target="term",
            option=option,
            names=names,
            values=values)

    def on_term_plain_sumti(self, target, option, names, values):
        """
        term_plain_sumti
            : sumti
        """
        return self.defaultNodeClass(
            target="term_plain_sumti",
            option=option,
            names=names,
            values=values)

    def on_term_placed_sumti(self, target, option, names, values):
        """
        term_placed_sumti
            : FA free_seq sumti
            | FA sumti
        """
        return self.defaultNodeClass(
            target="term_placed_sumti",
            option=option,
            names=names,
            values=values)

    def on_term_tagged_sumti(self, target, option, names, values):
        """
        term_tagged_sumti
            : tag sumti
        """
        return self.defaultNodeClass(
            target="term_tagged_sumti",
            option=option,
            names=names,
            values=values)

    def on_tagged_termset(self, target, option, names, values):
        """
        tagged_termset
            : tag termset
        """
        return self.defaultNodeClass(
            target="tagged_termset",
            option=option,
            names=names,
            values=values)

    def on_term_floating_tense(self, target, option, names, values):
        """
        term_floating_tense
            : tag KU free_seq
            | tag KU
            | tag /* ET KU */
        """
        return self.defaultNodeClass(
            target="term_floating_tense",
            option=option,
            names=names,
            values=values)

    def on_term_floating_negate(self, target, option, names, values):
        """
        term_floating_negate
            : PRIVATE_NA_KU NA KU free_seq
            | PRIVATE_NA_KU NA KU
        """
        return self.defaultNodeClass(
            target="term_floating_negate",
            option=option,
            names=names,
            values=values)

    def on_term_other(self, target, option, names, values):
        """
        term_other
            : FA free_seq KU free_seq
            | FA free_seq KU
            | FA free_seq /* ET KU */
            | FA KU free_seq
            | FA KU
            | FA /* ET KU */
        """
        return self.defaultNodeClass(
            target="term_other",
            option=option,
            names=names,
            values=values)

    def on_termset(self, target, option, names, values):
        """
        termset
            : termset_start gek termset_body gik termset_body
            | termset_start termset_body
        """
        return self.defaultNodeClass(
            target="termset",
            option=option,
            names=names,
            values=values)

    def on_termset_start(self, target, option, names, values):
        """
        termset_start
            : NUhI free_seq
            | NUhI
        """
        return self.defaultNodeClass(
            target="termset_start",
            option=option,
            names=names,
            values=values)

    def on_termset_body(self, target, option, names, values):
        """
        termset_body
            : terms NUhU free_seq
            | terms NUhU
            | terms /* ET NUhU */
        """
        return self.defaultNodeClass(
            target="termset_body",
            option=option,
            names=names,
            values=values)

    def on_sumti(self, target, option, names, values):
        """
        sumti
            : sumti_1
            | sumti_1 VUhO free_seq relative_clauses
            | sumti_1 VUhO relative_clauses
        """
        return self.defaultNodeClass(
            target="sumti",
            option=option,
            names=names,
            values=values)

    def on_sumti_1(self, target, option, names, values):
        """
        sumti_1
            : sumti_2
            | sumti_2 joik_ek_ke ke_sumti
        """
        return self.defaultNodeClass(
            target="sumti_1",
            option=option,
            names=names,
            values=values)

    def on_joik_ek_ke(self, target, option, names, values):
        """
        joik_ek_ke
            : PRIVATE_JOIK_KE joik stag
            | PRIVATE_JOIK_KE joik
            | PRIVATE_EK_KE ek stag
            | PRIVATE_EK_KE ek
        """
        return self.defaultNodeClass(
            target="joik_ek_ke",
            option=option,
            names=names,
            values=values)

    def on_ke_sumti(self, target, option, names, values):
        """
        ke_sumti
            : KE free_seq sumti KEhE free_seq
            | KE free_seq sumti KEhE
            | KE free_seq sumti /* ET KEhE */
            | KE sumti KEhE free_seq
            | KE sumti KEhE
            | KE sumti /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="ke_sumti",
            option=option,
            names=names,
            values=values)

    def on_sumti_2(self, target, option, names, values):
        """
        sumti_2
            : sumti_3
            | sumti_2 joik free_seq sumti_3
            | sumti_2 joik sumti_3
            | sumti_2 ek free_seq sumti_3
            | sumti_2 ek sumti_3
        """
        return self.defaultNodeClass(
            target="sumti_2",
            option=option,
            names=names,
            values=values)

    def on_sumti_3(self, target, option, names, values):
        """
        sumti_3
            : sumti_4
            | sumti_4 joik_ek_stag_bo sumti_3
        """
        return self.defaultNodeClass(
            target="sumti_3",
            option=option,
            names=names,
            values=values)

    def on_joik_ek_stag_bo(self, target, option, names, values):
        """
        joik_ek_stag_bo
            : PRIVATE_JOIK_BO joik stag BO free_seq
            | PRIVATE_JOIK_BO joik stag BO
            | PRIVATE_JOIK_BO joik BO free_seq
            | PRIVATE_JOIK_BO joik BO
            | PRIVATE_EK_BO ek stag BO free_seq
            | PRIVATE_EK_BO ek stag BO
            | PRIVATE_EK_BO ek BO free_seq
            | PRIVATE_EK_BO ek BO
        """
        return self.defaultNodeClass(
            target="joik_ek_stag_bo",
            option=option,
            names=names,
            values=values)

    def on_sumti_4(self, target, option, names, values):
        """
        sumti_4
            : sumti_5
            | gek sumti gik sumti_4
        """
        return self.defaultNodeClass(
            target="sumti_4",
            option=option,
            names=names,
            values=values)

    def on_sumti_5(self, target, option, names, values):
        """
        sumti_5
            : sumti_5a relative_clauses
            | sumti_5a
            | sumti_5b relative_clauses
            | sumti_5b
        """
        return self.defaultNodeClass(
            target="sumti_5",
            option=option,
            names=names,
            values=values)

    def on_sumti_5a(self, target, option, names, values):
        """
        sumti_5a
            : quantifier sumti_6
            | sumti_6
        """
        return self.defaultNodeClass(
            target="sumti_5a",
            option=option,
            names=names,
            values=values)

    def on_sumti_5b(self, target, option, names, values):
        """
        sumti_5b
            : quantifier selbri KU free_seq
            | quantifier selbri KU
            | quantifier selbri /* ET KU */
        """
        return self.defaultNodeClass(
            target="sumti_5b",
            option=option,
            names=names,
            values=values)

    def on_sumti_6(self, target, option, names, values):
        """
        sumti_6
            : lahe_sumti_6
            | nahe_bo_sumti_6
            | KOhA free_seq
            | KOhA
            | lerfu_string BOI free_seq
            | lerfu_string BOI
            | lerfu_string /* ET BOI */
            | LE free_seq sumti_tail KU free_seq
            | LE free_seq sumti_tail KU
            | LE free_seq sumti_tail /* ET KU */
            | LE sumti_tail KU free_seq
            | LE sumti_tail KU
            | LE sumti_tail /* ET KU */
            | LA free_seq sumti_tail KU free_seq
            | LA free_seq sumti_tail KU
            | LA free_seq sumti_tail /* ET KU */
            | LA sumti_tail KU free_seq
            | LA sumti_tail KU
            | LA sumti_tail /* ET KU */
            | name_sumti_6
            | LI free_seq mex LOhO free_seq
            | LI free_seq mex LOhO
            | LI free_seq mex /* ET LOhO */
            | LI mex LOhO free_seq
            | LI mex LOhO
            | LI mex /* ET LOhO */
            | ZO free_seq /* Needs lexer tie-in */
            | ZO /* Needs lexer tie-in */
            | LU text LIhU free_seq
            | LU text LIhU
            | LU text /* ET LIhU */
            | LOhU free_seq /* Needs lexer tie-in */
            | LOhU /* Needs lexer tie-in */
            | ZOI free_seq /* Needs lexer tie-in */
            | ZOI /* Needs lexer tie-in */
        """
        return self.defaultNodeClass(
            target="sumti_6",
            option=option,
            names=names,
            values=values)

    def on_lahe_sumti_6(self, target, option, names, values):
        """
        lahe_sumti_6
            : LAhE free_seq relative_clauses sumti LUhU free_seq
            | LAhE free_seq relative_clauses sumti LUhU
            | LAhE free_seq relative_clauses sumti /* ET LUhU */
            | LAhE free_seq sumti LUhU free_seq
            | LAhE free_seq sumti LUhU
            | LAhE free_seq sumti /* ET LUhU */
            | LAhE relative_clauses sumti LUhU free_seq
            | LAhE relative_clauses sumti LUhU
            | LAhE relative_clauses sumti /* ET LUhU */
            | LAhE sumti LUhU free_seq
            | LAhE sumti LUhU
            | LAhE sumti /* ET LUhU */
        """
        return self.defaultNodeClass(
            target="lahe_sumti_6",
            option=option,
            names=names,
            values=values)

    def on_nahe_bo_sumti_6(self, target, option, names, values):
        """
        nahe_bo_sumti_6
            : PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti LUhU
            | PRIVATE_NAhE_BO NAhE BO free_seq relative_clauses sumti /* ET LUhU */
            | PRIVATE_NAhE_BO NAhE BO free_seq sumti LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO free_seq sumti LUhU
            | PRIVATE_NAhE_BO NAhE BO free_seq sumti /* ET LUhU */
            | PRIVATE_NAhE_BO NAhE BO relative_clauses sumti LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO relative_clauses sumti LUhU
            | PRIVATE_NAhE_BO NAhE BO relative_clauses sumti /* ET LUhU */
            | PRIVATE_NAhE_BO NAhE BO sumti LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO sumti LUhU
            | PRIVATE_NAhE_BO NAhE BO sumti /* ET LUhU */
        """
        return self.defaultNodeClass(
            target="nahe_bo_sumti_6",
            option=option,
            names=names,
            values=values)

    def on_name_sumti_6(self, target, option, names, values):
        """
        name_sumti_6
            : LA free_seq relative_clauses CMENE_seq free_seq
            | LA free_seq relative_clauses CMENE_seq
            | LA free_seq CMENE_seq free_seq
            | LA free_seq CMENE_seq
            | LA relative_clauses CMENE_seq free_seq
            | LA relative_clauses CMENE_seq
            | LA CMENE_seq free_seq
            | LA CMENE_seq
        """
        return self.defaultNodeClass(
            target="name_sumti_6",
            option=option,
            names=names,
            values=values)

    def on_sumti_tail(self, target, option, names, values):
        """
        sumti_tail
            : sumti_6 relative_clauses sumti_tail_1
            | sumti_6 sumti_tail_1
            | sumti_tail_1
            | relative_clauses sumti_tail_1
        """
        return self.defaultNodeClass(
            target="sumti_tail",
            option=option,
            names=names,
            values=values)

    def on_sumti_tail_1(self, target, option, names, values):
        """
        sumti_tail_1
            : sumti_tail_1A relative_clauses
            | sumti_tail_1A
            | quantifier sumti
        """
        return self.defaultNodeClass(
            target="sumti_tail_1",
            option=option,
            names=names,
            values=values)

    def on_sumti_tail_1A(self, target, option, names, values):
        """
        sumti_tail_1A
            : quantifier selbri
            | selbri
        """
        return self.defaultNodeClass(
            target="sumti_tail_1A",
            option=option,
            names=names,
            values=values)

    def on_relative_clauses(self, target, option, names, values):
        """
        relative_clauses
            : relative_clause_seq
        """
        return self.defaultNodeClass(
            target="relative_clauses",
            option=option,
            names=names,
            values=values)

    def on_relative_clause_seq(self, target, option, names, values):
        """
        relative_clause_seq
            : relative_clause
            | relative_clause_seq ZIhE free_seq relative_clause
            | relative_clause_seq ZIhE relative_clause
        """
        return self.defaultNodeClass(
            target="relative_clause_seq",
            option=option,
            names=names,
            values=values)

    def on_relative_clause(self, target, option, names, values):
        """
        relative_clause
            : term_relative_clause
            | full_relative_clause
        """
        return self.defaultNodeClass(
            target="relative_clause",
            option=option,
            names=names,
            values=values)

    def on_term_relative_clause(self, target, option, names, values):
        """
        term_relative_clause
            : GOI free_seq term GEhU free_seq
            | GOI free_seq term GEhU
            | GOI free_seq term /* ET GEhU */
            | GOI term GEhU free_seq
            | GOI term GEhU
            | GOI term /* ET GEhU */
        """
        return self.defaultNodeClass(
            target="term_relative_clause",
            option=option,
            names=names,
            values=values)

    def on_full_relative_clause(self, target, option, names, values):
        """
        full_relative_clause
            : NOI free_seq subsentence KUhO free_seq
            | NOI free_seq subsentence KUhO
            | NOI free_seq subsentence /* ET KUhO */
            | NOI subsentence KUhO free_seq
            | NOI subsentence KUhO
            | NOI subsentence /* ET KUhO */
        """
        return self.defaultNodeClass(
            target="full_relative_clause",
            option=option,
            names=names,
            values=values)

    def on_selbri(self, target, option, names, values):
        """
        selbri
            : tag selbri_1
            | selbri_1
        """
        return self.defaultNodeClass(
            target="selbri",
            option=option,
            names=names,
            values=values)

    def on_selbri_1(self, target, option, names, values):
        """
        selbri_1
            : selbri_2
            | NA free_seq selbri
            | NA selbri
        """
        return self.defaultNodeClass(
            target="selbri_1",
            option=option,
            names=names,
            values=values)

    def on_selbri_2(self, target, option, names, values):
        """
        selbri_2
            : selbri_3 CO free_seq selbri_2
            | selbri_3 CO selbri_2
            | selbri_3
        """
        return self.defaultNodeClass(
            target="selbri_2",
            option=option,
            names=names,
            values=values)

    def on_selbri_3(self, target, option, names, values):
        """
        selbri_3
            : selbri_3 selbri_4
            | selbri_4
        """
        return self.defaultNodeClass(
            target="selbri_3",
            option=option,
            names=names,
            values=values)

    def on_selbri_4(self, target, option, names, values):
        """
        selbri_4
            : selbri_5
            | selbri_4 joik_opt_ke free_seq selbri_5
            | selbri_4 joik_opt_ke selbri_5
            | selbri_4 jek_opt_ke free_seq selbri_5
            | selbri_4 jek_opt_ke selbri_5
            | selbri_4 joik_stag_ke ke_selbri_3
        """
        return self.defaultNodeClass(
            target="selbri_4",
            option=option,
            names=names,
            values=values)

    def on_joik_stag_ke(self, target, option, names, values):
        """
        joik_stag_ke
            : PRIVATE_JOIK_KE joik stag
        """
        return self.defaultNodeClass(
            target="joik_stag_ke",
            option=option,
            names=names,
            values=values)

    def on_ke_selbri_3(self, target, option, names, values):
        """
        ke_selbri_3
            : KE free_seq selbri_3 KEhE free_seq
            | KE free_seq selbri_3 KEhE
            | KE free_seq selbri_3 /* ET KEhE */
            | KE selbri_3 KEhE free_seq
            | KE selbri_3 KEhE
            | KE selbri_3 /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="ke_selbri_3",
            option=option,
            names=names,
            values=values)

    def on_selbri_5(self, target, option, names, values):
        """
        selbri_5
            : selbri_6
            | selbri_6 joik_jek_stag_bo selbri_5
        """
        return self.defaultNodeClass(
            target="selbri_5",
            option=option,
            names=names,
            values=values)

    def on_joik_jek_stag_bo(self, target, option, names, values):
        """
        joik_jek_stag_bo
            : PRIVATE_JOIK_BO joik stag BO free_seq
            | PRIVATE_JOIK_BO joik stag BO
            | PRIVATE_JOIK_BO joik BO free_seq
            | PRIVATE_JOIK_BO joik BO
            | PRIVATE_JEK_BO jek stag BO free_seq
            | PRIVATE_JEK_BO jek stag BO
            | PRIVATE_JEK_BO jek BO free_seq
            | PRIVATE_JEK_BO jek BO
        """
        return self.defaultNodeClass(
            target="joik_jek_stag_bo",
            option=option,
            names=names,
            values=values)

    def on_selbri_6(self, target, option, names, values):
        """
        selbri_6
            : tanru_unit
            | tanru_unit BO free_seq selbri_6
            | tanru_unit BO selbri_6
            | NAhE free_seq guhek selbri gik selbri_6
            | NAhE guhek selbri gik selbri_6
            | guhek selbri gik selbri_6
        """
        return self.defaultNodeClass(
            target="selbri_6",
            option=option,
            names=names,
            values=values)

    def on_tanru_unit(self, target, option, names, values):
        """
        tanru_unit
            : tanru_unit_1
            | tanru_unit CEI free_seq tanru_unit_1
            | tanru_unit CEI tanru_unit_1
        """
        return self.defaultNodeClass(
            target="tanru_unit",
            option=option,
            names=names,
            values=values)

    def on_tanru_unit_1(self, target, option, names, values):
        """
        tanru_unit_1
            : tanru_unit_2
            | tanru_unit_2 linkargs
        """
        return self.defaultNodeClass(
            target="tanru_unit_1",
            option=option,
            names=names,
            values=values)

    def on_tanru_unit_2(self, target, option, names, values):
        """
        tanru_unit_2
            : BRIVLA free_seq
            | BRIVLA
            | GOhA RAhO free_seq
            | GOhA RAhO
            | GOhA free_seq
            | GOhA
            | ke_selbri3_tu2
            | ME free_seq sumti MEhU free_seq MOI free_seq
            | ME free_seq sumti MEhU free_seq MOI
            | ME free_seq sumti MEhU free_seq
            | ME free_seq sumti MEhU MOI free_seq
            | ME free_seq sumti MEhU MOI
            | ME free_seq sumti MEhU
            | ME free_seq sumti /* ET MEhU */ MOI free_seq
            | ME free_seq sumti /* ET MEhU */ MOI
            | ME free_seq sumti /* ET MEhU */
            | ME sumti MEhU free_seq MOI free_seq
            | ME sumti MEhU free_seq MOI
            | ME sumti MEhU free_seq
            | ME sumti MEhU MOI free_seq
            | ME sumti MEhU MOI
            | ME sumti MEhU
            | ME sumti /* ET MEhU */ MOI free_seq
            | ME sumti /* ET MEhU */ MOI
            | ME sumti /* ET MEhU */
            | number_moi_tu2
            | NUhA free_seq mex_operator
            | NUhA mex_operator
            | se_tu2
            | jai_tag_tu2
            | jai_tu2
            | ZEI /* needs lexical tie-in */
            | nahe_tu2
            | abstraction
        """
        return self.defaultNodeClass(
            target="tanru_unit_2",
            option=option,
            names=names,
            values=values)

    def on_ke_selbri3_tu2(self, target, option, names, values):
        """
        ke_selbri3_tu2
            : KE free_seq selbri_3 KEhE free_seq
            | KE free_seq selbri_3 KEhE
            | KE free_seq selbri_3 /* ET KEhE */
            | KE selbri_3 KEhE free_seq
            | KE selbri_3 KEhE
            | KE selbri_3 /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="ke_selbri3_tu2",
            option=option,
            names=names,
            values=values)

    def on_number_moi_tu2(self, target, option, names, values):
        """
        number_moi_tu2
            : PRIVATE_NUMBER_MOI number MOI free_seq
            | PRIVATE_NUMBER_MOI number MOI
            | PRIVATE_NUMBER_MOI lerfu_string MOI free_seq
            | PRIVATE_NUMBER_MOI lerfu_string MOI
        """
        return self.defaultNodeClass(
            target="number_moi_tu2",
            option=option,
            names=names,
            values=values)

    def on_se_tu2(self, target, option, names, values):
        """
        se_tu2
            : SE free_seq tanru_unit_2
            | SE tanru_unit_2
        """
        return self.defaultNodeClass(
            target="se_tu2",
            option=option,
            names=names,
            values=values)

    def on_jai_tag_tu2(self, target, option, names, values):
        """
        jai_tag_tu2
            : JAI free_seq tag tanru_unit_2
            | JAI tag tanru_unit_2
        """
        return self.defaultNodeClass(
            target="jai_tag_tu2",
            option=option,
            names=names,
            values=values)

    def on_jai_tu2(self, target, option, names, values):
        """
        jai_tu2
            : JAI free_seq tanru_unit_2
            | JAI tanru_unit_2
        """
        return self.defaultNodeClass(
            target="jai_tu2",
            option=option,
            names=names,
            values=values)

    def on_nahe_tu2(self, target, option, names, values):
        """
        nahe_tu2
            : NAhE free_seq tanru_unit_2
            | NAhE tanru_unit_2
        """
        return self.defaultNodeClass(
            target="nahe_tu2",
            option=option,
            names=names,
            values=values)

    def on_abstraction(self, target, option, names, values):
        """
        abstraction
            : nu_nai_seq subsentence KEI free_seq
            | nu_nai_seq subsentence KEI
            | nu_nai_seq subsentence /* ET KEI */
        """
        return self.defaultNodeClass(
            target="abstraction",
            option=option,
            names=names,
            values=values)

    def on_nu_nai_seq(self, target, option, names, values):
        """
        nu_nai_seq
            : NU NAI free_seq
            | NU free_seq
            | NU NAI
            | NU
            | nu_nai_seq joik free_seq NU NAI free_seq
            | nu_nai_seq joik free_seq NU NAI
            | nu_nai_seq joik free_seq NU free_seq
            | nu_nai_seq joik free_seq NU
            | nu_nai_seq joik NU NAI free_seq
            | nu_nai_seq joik NU NAI
            | nu_nai_seq joik NU free_seq
            | nu_nai_seq joik NU
            | nu_nai_seq jek free_seq NU NAI free_seq
            | nu_nai_seq jek free_seq NU NAI
            | nu_nai_seq jek free_seq NU free_seq
            | nu_nai_seq jek free_seq NU
            | nu_nai_seq jek NU NAI free_seq
            | nu_nai_seq jek NU NAI
            | nu_nai_seq jek NU free_seq
            | nu_nai_seq jek NU
        """
        return self.defaultNodeClass(
            target="nu_nai_seq",
            option=option,
            names=names,
            values=values)

    def on_linkargs(self, target, option, names, values):
        """
        linkargs
            : BE free_seq term links BEhO free_seq
            | BE free_seq term links BEhO
            | BE free_seq term links /* ET BEhO */
            | BE term links BEhO free_seq
            | BE term links BEhO
            | BE term links /* ET BEhO */
            | BE free_seq term BEhO free_seq
            | BE free_seq term BEhO
            | BE free_seq term /* ET BEhO */
            | BE term BEhO free_seq
            | BE term BEhO
            | BE term /* ET BEhO */
        """
        return self.defaultNodeClass(
            target="linkargs",
            option=option,
            names=names,
            values=values)

    def on_links(self, target, option, names, values):
        """
        links
            : BEI free_seq term links
            | BEI term links
            | BEI free_seq term
            | BEI term
        """
        return self.defaultNodeClass(
            target="links",
            option=option,
            names=names,
            values=values)

    def on_quantifier(self, target, option, names, values):
        """
        quantifier
            : number BOI free_seq
            | number BOI
            | number /* ET BOI */
            | VEI free_seq mex VEhO free_seq
            | VEI free_seq mex VEhO
            | VEI free_seq mex /* ET VEhO */
            | VEI mex VEhO free_seq
            | VEI mex VEhO
            | VEI mex /* ET VEhO */
        """
        return self.defaultNodeClass(
            target="quantifier",
            option=option,
            names=names,
            values=values)

    def on_mex(self, target, option, names, values):
        """
        mex
            : mex_infix
            | mex_rp
        """
        return self.defaultNodeClass(
            target="mex",
            option=option,
            names=names,
            values=values)

    def on_mex_rp(self, target, option, names, values):
        """
        mex_rp
            : FUhA free_seq rp_expression
            | FUhA rp_expression
        """
        return self.defaultNodeClass(
            target="mex_rp",
            option=option,
            names=names,
            values=values)

    def on_mex_infix(self, target, option, names, values):
        """
        mex_infix
            : mex_1
            | mex_infix operator mex_1
        """
        return self.defaultNodeClass(
            target="mex_infix",
            option=option,
            names=names,
            values=values)

    def on_mex_1(self, target, option, names, values):
        """
        mex_1
            : mex_2
            | mex_2 BIhE free_seq operator mex_1
            | mex_2 BIhE operator mex_1
        """
        return self.defaultNodeClass(
            target="mex_1",
            option=option,
            names=names,
            values=values)

    def on_mex_2(self, target, option, names, values):
        """
        mex_2
            : operand
            | PEhO free_seq operator mex_2_seq KUhE free_seq
            | PEhO free_seq operator mex_2_seq KUhE
            | PEhO free_seq operator mex_2_seq /* ET KUhE */
            | PEhO operator mex_2_seq KUhE free_seq
            | PEhO operator mex_2_seq KUhE
            | PEhO operator mex_2_seq /* ET KUhE */
            | operator mex_2_seq KUhE free_seq
            | operator mex_2_seq KUhE
            | operator mex_2_seq /* ET KUhE */
        """
        return self.defaultNodeClass(
            target="mex_2",
            option=option,
            names=names,
            values=values)

    def on_mex_2_seq(self, target, option, names, values):
        """
        mex_2_seq
            : mex_2
            | mex_2_seq mex_2
        """
        return self.defaultNodeClass(
            target="mex_2_seq",
            option=option,
            names=names,
            values=values)

    def on_rp_expression(self, target, option, names, values):
        """
        rp_expression
            : rp_expression rp_expression operator
            | operand rp_expression operator
            | rp_expression operand operator
            | operand operand operator
        """
        return self.defaultNodeClass(
            target="rp_expression",
            option=option,
            names=names,
            values=values)

    def on_operator(self, target, option, names, values):
        """
        operator
            : operator_1
            | operator joik_opt_ke free_seq operator_1
            | operator joik_opt_ke operator_1
            | operator jek_opt_ke free_seq operator_1
            | operator jek_opt_ke operator_1
            | operator joik_stag_ke ke_operator
        """
        return self.defaultNodeClass(
            target="operator",
            option=option,
            names=names,
            values=values)

    def on_ke_operator(self, target, option, names, values):
        """
        ke_operator
            : KE free_seq operator KEhE free_seq
            | KE free_seq operator KEhE
            | KE free_seq operator /* ET KEhE */
            | KE operator KEhE free_seq
            | KE operator KEhE
            | KE operator /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="ke_operator",
            option=option,
            names=names,
            values=values)

    def on_operator_1(self, target, option, names, values):
        """
        operator_1
            : operator_2
            | guhek operator_1 gik operator_2
            | operator_2 joik_jek_stag_bo operator_1
        """
        return self.defaultNodeClass(
            target="operator_1",
            option=option,
            names=names,
            values=values)

    def on_operator_2(self, target, option, names, values):
        """
        operator_2
            : mex_operator
            | KE free_seq operator KEhE free_seq
            | KE free_seq operator KEhE
            | KE free_seq operator /* ET KEhE */
            | KE operator KEhE free_seq
            | KE operator KEhE
            | KE operator /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="operator_2",
            option=option,
            names=names,
            values=values)

    def on_mex_operator(self, target, option, names, values):
        """
        mex_operator
            : SE free_seq mex_operator
            | SE mex_operator
            | NAhE free_seq mex_operator
            | NAhE mex_operator
            | MAhO free_seq mex TEhU free_seq
            | MAhO free_seq mex TEhU
            | MAhO free_seq mex /* ET TEhU */
            | MAhO mex TEhU free_seq
            | MAhO mex TEhU
            | MAhO mex /* ET TEhU */
            | NAhU free_seq selbri TEhU free_seq
            | NAhU free_seq selbri TEhU
            | NAhU free_seq selbri /* ET TEhU */
            | NAhU selbri TEhU free_seq
            | NAhU selbri TEhU
            | NAhU selbri /* ET TEhU */
            | VUhU free_seq
            | VUhU
        """
        return self.defaultNodeClass(
            target="mex_operator",
            option=option,
            names=names,
            values=values)

    def on_operand(self, target, option, names, values):
        """
        operand
            : operand_1
            | operand_1 joik_ek_ke ke_operand
        """
        return self.defaultNodeClass(
            target="operand",
            option=option,
            names=names,
            values=values)

    def on_ke_operand(self, target, option, names, values):
        """
        ke_operand
            : KE free_seq operand KEhE free_seq
            | KE free_seq operand KEhE
            | KE free_seq operand /* ET KEhE */
            | KE operand KEhE free_seq
            | KE operand KEhE
            | KE operand /* ET KEhE */
        """
        return self.defaultNodeClass(
            target="ke_operand",
            option=option,
            names=names,
            values=values)

    def on_operand_1(self, target, option, names, values):
        """
        operand_1
            : operand_2
            | operand_1 joik free_seq operand_2
            | operand_1 joik operand_2
            | operand_1 jek free_seq operand_2
            | operand_1 jek operand_2
        """
        return self.defaultNodeClass(
            target="operand_1",
            option=option,
            names=names,
            values=values)

    def on_operand_2(self, target, option, names, values):
        """
        operand_2
            : operand_3
            | operand_3 joik_ek_stag_bo operand_2
        """
        return self.defaultNodeClass(
            target="operand_2",
            option=option,
            names=names,
            values=values)

    def on_operand_3(self, target, option, names, values):
        """
        operand_3
            : quantifier
            | lerfu_string BOI free_seq
            | lerfu_string BOI
            | lerfu_string /* ET BOI */
            | NIhE free_seq selbri TEhU free_seq
            | NIhE free_seq selbri TEhU
            | NIhE free_seq selbri /* ET TEhU */
            | NIhE selbri TEhU free_seq
            | NIhE selbri TEhU
            | NIhE selbri /* ET TEhU */
            | MOhE free_seq sumti TEhU free_seq
            | MOhE free_seq sumti TEhU
            | MOhE free_seq sumti /* ET TEhU */
            | MOhE sumti TEhU free_seq
            | MOhE sumti TEhU
            | MOhE sumti /* ET TEhU */
            | JOhI free_seq mex_2_seq TEhU free_seq
            | JOhI free_seq mex_2_seq TEhU
            | JOhI free_seq mex_2_seq /* ET TEhU */
            | JOhI mex_2_seq TEhU free_seq
            | JOhI mex_2_seq TEhU
            | JOhI mex_2_seq /* ET TEhU */
            | gek operand gik operand_3
            | LAhE free_seq operand LUhU free_seq
            | LAhE free_seq operand LUhU
            | LAhE free_seq operand /* ET LUhU */
            | LAhE operand LUhU free_seq
            | LAhE operand LUhU
            | LAhE operand /* ET LUhU */
            | PRIVATE_NAhE_BO NAhE BO free_seq operand LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO free_seq operand LUhU
            | PRIVATE_NAhE_BO NAhE BO free_seq operand /* ET LUhU */
            | PRIVATE_NAhE_BO NAhE BO operand LUhU free_seq
            | PRIVATE_NAhE_BO NAhE BO operand LUhU
            | PRIVATE_NAhE_BO NAhE BO operand /* ET LUhU */
        """
        return self.defaultNodeClass(
            target="operand_3",
            option=option,
            names=names,
            values=values)

    def on_number(self, target, option, names, values):
        """
        number
            : inner_number
        """
        return self.defaultNodeClass(
            target="number",
            option=option,
            names=names,
            values=values)

    def on_inner_number(self, target, option, names, values):
        """
        inner_number
            : PA
            | inner_number PA
            | inner_number lerfu_word
        """
        return self.defaultNodeClass(
            target="inner_number",
            option=option,
            names=names,
            values=values)

    def on_lerfu_string(self, target, option, names, values):
        """
        lerfu_string
            : lerfu_word
            | lerfu_string PA
            | lerfu_string lerfu_word
        """
        return self.defaultNodeClass(
            target="lerfu_string",
            option=option,
            names=names,
            values=values)

    def on_lerfu_word(self, target, option, names, values):
        """
        lerfu_word
            : BY
            | BU /* needs lexer tie-in */
            | LAU lerfu_word
            | TEI lerfu_string FOI
        """
        return self.defaultNodeClass(
            target="lerfu_word",
            option=option,
            names=names,
            values=values)

    def on_ek(self, target, option, names, values):
        """
        ek
            : PRIVATE_START_EK NA SE A NAI
            | PRIVATE_START_EK NA SE A
            | PRIVATE_START_EK NA A NAI
            | PRIVATE_START_EK NA A
            | PRIVATE_START_EK SE A NAI
            | PRIVATE_START_EK SE A
            | PRIVATE_START_EK A NAI
            | PRIVATE_START_EK A
        """
        return self.defaultNodeClass(
            target="ek",
            option=option,
            names=names,
            values=values)

    def on_gihek(self, target, option, names, values):
        """
        gihek
            : PRIVATE_START_GIHEK NA SE GIhA NAI
            | PRIVATE_START_GIHEK NA SE GIhA
            | PRIVATE_START_GIHEK NA GIhA NAI
            | PRIVATE_START_GIHEK NA GIhA
            | PRIVATE_START_GIHEK SE GIhA NAI
            | PRIVATE_START_GIHEK SE GIhA
            | PRIVATE_START_GIHEK GIhA NAI
            | PRIVATE_START_GIHEK GIhA
        """
        return self.defaultNodeClass(
            target="gihek",
            option=option,
            names=names,
            values=values)

    def on_jek(self, target, option, names, values):
        """
        jek
            : PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK JA PRIVATE_END_JEK
        """
        return self.defaultNodeClass(
            target="jek",
            option=option,
            names=names,
            values=values)

    def on_jek_opt_ke(self, target, option, names, values):
        """
        jek_opt_ke
            : PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK JA PRIVATE_END_JEK
        """
        return self.defaultNodeClass(
            target="jek_opt_ke",
            option=option,
            names=names,
            values=values)

    def on_jek_opt_kebo(self, target, option, names, values):
        """
        jek_opt_kebo
            : PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_START_JEK JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_KE PRIVATE_START_JEK JA PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK NA SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK NA SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK NA JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK NA JA PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK SE JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK SE JA PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK JA NAI PRIVATE_END_JEK
            | PRIVATE_JEK_BO PRIVATE_START_JEK JA PRIVATE_END_JEK
        """
        return self.defaultNodeClass(
            target="jek_opt_kebo",
            option=option,
            names=names,
            values=values)

    def on_joik(self, target, option, names, values):
        """
        joik
            : PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
        """
        return self.defaultNodeClass(
            target="joik",
            option=option,
            names=names,
            values=values)

    def on_joik_opt_ke(self, target, option, names, values):
        """
        joik_opt_ke
            : PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
        """
        return self.defaultNodeClass(
            target="joik_opt_ke",
            option=option,
            names=names,
            values=values)

    def on_joik_opt_kebo(self, target, option, names, values):
        """
        joik_opt_kebo
            : PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_KE PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK SE JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK SE JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK JOI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK JOI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK SE BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK SE BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK BIhI NAI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK BIhI PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO SE BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO SE BIhI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO BIhI NAI GAhO PRIVATE_END_JOIK
            | PRIVATE_JOIK_BO PRIVATE_START_JOIK GAhO BIhI GAhO PRIVATE_END_JOIK
        """
        return self.defaultNodeClass(
            target="joik_opt_kebo",
            option=option,
            names=names,
            values=values)

    def on_gek(self, target, option, names, values):
        """
        gek
            : PRIVATE_START_GEK SE GA NAI free_seq
            | PRIVATE_START_GEK SE GA NAI
            | PRIVATE_START_GEK SE GA free_seq
            | PRIVATE_START_GEK SE GA
            | PRIVATE_START_GEK GA NAI free_seq
            | PRIVATE_START_GEK GA NAI
            | PRIVATE_START_GEK GA free_seq
            | PRIVATE_START_GEK GA
            | PRIVATE_START_GEK joik GI free_seq
            | PRIVATE_START_GEK joik GI
            | PRIVATE_START_GEK stag gik
        """
        return self.defaultNodeClass(
            target="gek",
            option=option,
            names=names,
            values=values)

    def on_guhek(self, target, option, names, values):
        """
        guhek
            : PRIVATE_START_GUHEK SE GUhA NAI free_seq
            | PRIVATE_START_GUHEK SE GUhA NAI
            | PRIVATE_START_GUHEK SE GUhA free_seq
            | PRIVATE_START_GUHEK SE GUhA
            | PRIVATE_START_GUHEK GUhA NAI free_seq
            | PRIVATE_START_GUHEK GUhA NAI
            | PRIVATE_START_GUHEK GUhA free_seq
            | PRIVATE_START_GUHEK GUhA
        """
        return self.defaultNodeClass(
            target="guhek",
            option=option,
            names=names,
            values=values)

    def on_gik(self, target, option, names, values):
        """
        gik
            : GI NAI free_seq
            | GI NAI
            | GI free_seq
            | GI
        """
        return self.defaultNodeClass(
            target="gik",
            option=option,
            names=names,
            values=values)

    def on_tag(self, target, option, names, values):
        """
        tag
            : ctag
            | stag
        """
        return self.defaultNodeClass(
            target="tag",
            option=option,
            names=names,
            values=values)

    def on_ctag(self, target, option, names, values):
        """
        ctag
            : complex_tense_modal
            | ctag joik_opt_kebo free_seq complex_tense_modal
            | ctag joik_opt_kebo complex_tense_modal
            | ctag jek_opt_kebo free_seq complex_tense_modal
            | ctag jek_opt_kebo complex_tense_modal
            | ctag joik_opt_kebo free_seq simple_tense_modal
            | ctag joik_opt_kebo simple_tense_modal
            | ctag jek_opt_kebo free_seq simple_tense_modal
            | ctag jek_opt_kebo simple_tense_modal
            | stag joik_opt_kebo free_seq complex_tense_modal
            | stag joik_opt_kebo complex_tense_modal
            | stag jek_opt_kebo free_seq complex_tense_modal
            | stag jek_opt_kebo complex_tense_modal
        """
        return self.defaultNodeClass(
            target="ctag",
            option=option,
            names=names,
            values=values)

    def on_complex_tense_modal(self, target, option, names, values):
        """
        complex_tense_modal
            : FIhO free_seq selbri FEhU free_seq
            | FIhO free_seq selbri FEhU
            | FIhO free_seq selbri /* ET FEhU */
            | FIhO selbri FEhU free_seq
            | FIhO selbri FEhU
            | FIhO selbri /* ET FEhU */
            | simple_tense_modal free_seq
        """
        return self.defaultNodeClass(
            target="complex_tense_modal",
            option=option,
            names=names,
            values=values)

    def on_stag(self, target, option, names, values):
        """
        stag
            : simple_tense_modal
            | stag jek_opt_kebo simple_tense_modal
            | stag joik_opt_kebo simple_tense_modal
        """
        return self.defaultNodeClass(
            target="stag",
            option=option,
            names=names,
            values=values)

    def on_simple_tense_modal(self, target, option, names, values):
        """
        simple_tense_modal
            : PRIVATE_START_TENSE NAhE se_bai NAI KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE se_bai NAI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE se_bai KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE se_bai PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE bai1 NAI KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE bai1 NAI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE bai1 KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE bai1 PRIVATE_END_TENSE
            | PRIVATE_START_TENSE se_bai NAI KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE se_bai NAI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE se_bai KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE se_bai PRIVATE_END_TENSE
            | PRIVATE_START_TENSE bai1 NAI KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE bai1 NAI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE bai1 KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE bai1 PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time space CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time space CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time space KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time space PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE time PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time space CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time space CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time space KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time space PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE time PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space time CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space time CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space time KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space time PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE space PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space time CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space time CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space time KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space time PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE space PRIVATE_END_TENSE
            | PRIVATE_START_TENSE CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE CAhA KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE NAhE CAhA PRIVATE_END_TENSE
            | PRIVATE_START_TENSE KI PRIVATE_END_TENSE
            | PRIVATE_START_TENSE CUhE PRIVATE_END_TENSE
        """
        return self.defaultNodeClass(
            target="simple_tense_modal",
            option=option,
            names=names,
            values=values)

    def on_se_bai(self, target, option, names, values):
        """
        se_bai
            : SE BAI
        """
        return self.defaultNodeClass(
            target="se_bai",
            option=option,
            names=names,
            values=values)

    def on_bai1(self, target, option, names, values):
        """
        bai1
            : BAI
        """
        return self.defaultNodeClass(
            target="bai1",
            option=option,
            names=names,
            values=values)

    def on_time(self, target, option, names, values):
        """
        time
            : ZI time_offset_seq zeha_pu_nai interval_property_seq
            | ZI time_offset_seq interval_property_seq
            | ZI time_offset_seq zeha_pu_nai
            | ZI time_offset_seq
            | ZI zeha_pu_nai interval_property_seq
            | ZI interval_property_seq
            | ZI zeha_pu_nai
            | ZI
            | time_offset_seq zeha_pu_nai interval_property_seq
            | time_offset_seq interval_property_seq
            | time_offset_seq zeha_pu_nai
            | time_offset_seq
            | zeha_pu_nai interval_property_seq
            | interval_property_seq
            | zeha_pu_nai
        """
        return self.defaultNodeClass(
            target="time",
            option=option,
            names=names,
            values=values)

    def on_zeha_pu_nai(self, target, option, names, values):
        """
        zeha_pu_nai
            : ZEhA PU NAI
            | ZEhA PU
            | ZEhA
        """
        return self.defaultNodeClass(
            target="zeha_pu_nai",
            option=option,
            names=names,
            values=values)

    def on_time_offset(self, target, option, names, values):
        """
        time_offset
            : PU NAI ZI
            | PU NAI
            | PU ZI
            | PU
        """
        return self.defaultNodeClass(
            target="time_offset",
            option=option,
            names=names,
            values=values)

    def on_time_offset_seq(self, target, option, names, values):
        """
        time_offset_seq
            : time_offset_seq time_offset
            | time_offset
        """
        return self.defaultNodeClass(
            target="time_offset_seq",
            option=option,
            names=names,
            values=values)

    def on_space(self, target, option, names, values):
        """
        space
            : VA space_offset_seq space_interval MOhI space_offset
            | VA space_offset_seq space_interval
            | VA space_offset_seq MOhI space_offset
            | VA space_offset_seq
            | VA space_interval MOhI space_offset
            | VA space_interval
            | VA MOhI space_offset
            | VA
            | space_offset_seq space_interval MOhI space_offset
            | space_offset_seq space_interval
            | space_offset_seq MOhI space_offset
            | space_offset_seq
            | space_interval MOhI space_offset
            | space_interval
            | MOhI space_offset
        """
        return self.defaultNodeClass(
            target="space",
            option=option,
            names=names,
            values=values)

    def on_space_offset(self, target, option, names, values):
        """
        space_offset
            : FAhA NAI VA
            | FAhA NAI
            | FAhA VA
            | FAhA
        """
        return self.defaultNodeClass(
            target="space_offset",
            option=option,
            names=names,
            values=values)

    def on_space_offset_seq(self, target, option, names, values):
        """
        space_offset_seq
            : space_offset_seq space_offset
            | space_offset
        """
        return self.defaultNodeClass(
            target="space_offset_seq",
            option=option,
            names=names,
            values=values)

    def on_space_interval(self, target, option, names, values):
        """
        space_interval
            : VEhA VIhA FAhA NAI space_int_props
            | VEhA VIhA FAhA space_int_props
            | VEhA VIhA space_int_props
            | VEhA FAhA NAI space_int_props
            | VEhA FAhA space_int_props
            | VEhA space_int_props
            | VIhA FAhA NAI space_int_props
            | VIhA FAhA space_int_props
            | VIhA space_int_props
            | VEhA VIhA FAhA NAI
            | VEhA VIhA FAhA
            | VEhA VIhA
            | VEhA FAhA NAI
            | VEhA FAhA
            | VEhA
            | VIhA FAhA NAI
            | VIhA FAhA
            | VIhA
            | space_int_props
        """
        return self.defaultNodeClass(
            target="space_interval",
            option=option,
            names=names,
            values=values)

    def on_space_int_props(self, target, option, names, values):
        """
        space_int_props
            : space_int_props space_int_prop
            | space_int_prop
        """
        return self.defaultNodeClass(
            target="space_int_props",
            option=option,
            names=names,
            values=values)

    def on_space_int_prop(self, target, option, names, values):
        """
        space_int_prop
            : FEhE interval_property
        """
        return self.defaultNodeClass(
            target="space_int_prop",
            option=option,
            names=names,
            values=values)

    def on_interval_property(self, target, option, names, values):
        """
        interval_property
            : PRIVATE_NUMBER_ROI number ROI NAI
            | PRIVATE_NUMBER_ROI number ROI
            | TAhE NAI
            | TAhE
            | ZAhO NAI
            | ZAhO
        """
        return self.defaultNodeClass(
            target="interval_property",
            option=option,
            names=names,
            values=values)

    def on_interval_property_seq(self, target, option, names, values):
        """
        interval_property_seq
            : interval_property_seq interval_property
            | interval_property
        """
        return self.defaultNodeClass(
            target="interval_property_seq",
            option=option,
            names=names,
            values=values)

    def on_free_seq(self, target, option, names, values):
        """
        free_seq
            : free_seq free
            | free
        """
        return self.defaultNodeClass(
            target="free_seq",
            option=option,
            names=names,
            values=values)

    def on_free(self, target, option, names, values):
        """
        free
            : metalinguistic
            | reciprocity
            | free_vocative
            | utterance_ordinal
            | parenthetical
            | subscript
        """
        return self.defaultNodeClass(
            target="free",
            option=option,
            names=names,
            values=values)

    def on_metalinguistic(self, target, option, names, values):
        """
        metalinguistic
            : SEI free_seq terms CU free_seq metalinguistic_main_selbri SEhU
            | SEI free_seq terms CU free_seq metalinguistic_main_selbri /* ET SEhU */
            | SEI free_seq terms CU metalinguistic_main_selbri SEhU
            | SEI free_seq terms CU metalinguistic_main_selbri /* ET SEhU */
            | SEI free_seq terms metalinguistic_main_selbri SEhU
            | SEI free_seq terms metalinguistic_main_selbri /* ET SEhU */
            | SEI free_seq metalinguistic_main_selbri SEhU
            | SEI free_seq metalinguistic_main_selbri /* ET SEhU */
            | SEI terms CU free_seq metalinguistic_main_selbri SEhU
            | SEI terms CU free_seq metalinguistic_main_selbri /* ET SEhU */
            | SEI terms CU metalinguistic_main_selbri SEhU
            | SEI terms CU metalinguistic_main_selbri /* ET SEhU */
            | SEI terms metalinguistic_main_selbri SEhU
            | SEI terms metalinguistic_main_selbri /* ET SEhU */
            | SEI metalinguistic_main_selbri SEhU
            | SEI metalinguistic_main_selbri /* ET SEhU */
        """
        return self.defaultNodeClass(
            target="metalinguistic",
            option=option,
            names=names,
            values=values)

    def on_metalinguistic_main_selbri(self, target, option, names, values):
        """
        metalinguistic_main_selbri
            : selbri
        """
        return self.defaultNodeClass(
            target="metalinguistic_main_selbri",
            option=option,
            names=names,
            values=values)

    def on_reciprocity(self, target, option, names, values):
        """
        reciprocity
            : SOI free_seq sumti sumti SEhU
            | SOI free_seq sumti sumti /* ET SEhU */
            | SOI free_seq sumti SEhU
            | SOI free_seq sumti /* ET SEhU */
            | SOI sumti sumti SEhU
            | SOI sumti sumti /* ET SEhU */
            | SOI sumti SEhU
            | SOI sumti /* ET SEhU */
        """
        return self.defaultNodeClass(
            target="reciprocity",
            option=option,
            names=names,
            values=values)

    def on_free_vocative(self, target, option, names, values):
        """
        free_vocative
            : vocative relative_clauses selbri relative_clauses DOhU
            | vocative relative_clauses selbri relative_clauses /* ET DOhU */
            | vocative relative_clauses selbri DOhU
            | vocative relative_clauses selbri /* ET DOhU */
            | vocative selbri relative_clauses DOhU
            | vocative selbri relative_clauses /* ET DOhU */
            | vocative selbri DOhU
            | vocative selbri /* ET DOhU */
            | vocative relative_clauses CMENE_seq free_seq relative_clauses DOhU
            | vocative relative_clauses CMENE_seq free_seq relative_clauses /* ET DOhU */
            | vocative relative_clauses CMENE_seq free_seq DOhU
            | vocative relative_clauses CMENE_seq free_seq /* ET DOhU */
            | vocative CMENE_seq free_seq relative_clauses DOhU
            | vocative CMENE_seq free_seq relative_clauses /* ET DOhU */
            | vocative CMENE_seq free_seq DOhU
            | vocative CMENE_seq free_seq /* ET DOhU */
            | vocative relative_clauses CMENE_seq relative_clauses DOhU
            | vocative relative_clauses CMENE_seq relative_clauses /* ET DOhU */
            | vocative relative_clauses CMENE_seq DOhU
            | vocative relative_clauses CMENE_seq /* ET DOhU */
            | vocative CMENE_seq relative_clauses DOhU
            | vocative CMENE_seq relative_clauses /* ET DOhU */
            | vocative CMENE_seq DOhU
            | vocative CMENE_seq /* ET DOhU */
            | vocative sumti DOhU
            | vocative sumti /* ET DOhU */
            | vocative DOhU
            | vocative /* ET DOhU */
        """
        return self.defaultNodeClass(
            target="free_vocative",
            option=option,
            names=names,
            values=values)

    def on_utterance_ordinal(self, target, option, names, values):
        """
        utterance_ordinal
            : PRIVATE_NUMBER_MAI number MAI
            | PRIVATE_NUMBER_MAI lerfu_string MAI
        """
        return self.defaultNodeClass(
            target="utterance_ordinal",
            option=option,
            names=names,
            values=values)

    def on_parenthetical(self, target, option, names, values):
        """
        parenthetical
            : TO text TOI
            | TO text /* ET TOI */
        """
        return self.defaultNodeClass(
            target="parenthetical",
            option=option,
            names=names,
            values=values)

    def on_subscript(self, target, option, names, values):
        """
        subscript
            : XI free_seq number BOI
            | XI free_seq number /* ET BOI */
            | XI number BOI
            | XI number /* ET BOI */
            | XI free_seq lerfu_string BOI
            | XI free_seq lerfu_string /* ET BOI */
            | XI lerfu_string BOI
            | XI lerfu_string /* ET BOI */
            | XI free_seq VEI free_seq mex VEhO
            | XI free_seq VEI free_seq mex /* ET VEhO */
            | XI free_seq VEI mex VEhO
            | XI free_seq VEI mex /* ET VEhO */
            | XI VEI free_seq mex VEhO
            | XI VEI free_seq mex /* ET VEhO */
            | XI VEI mex VEhO
            | XI VEI mex /* ET VEhO */
        """
        return self.defaultNodeClass(
            target="subscript",
            option=option,
            names=names,
            values=values)

    def on_vocative(self, target, option, names, values):
        """
        vocative
            : coi_nai_seq DOI
            | coi_nai_seq
            | DOI
        """
        return self.defaultNodeClass(
            target="vocative",
            option=option,
            names=names,
            values=values)

    def on_coi_nai_seq(self, target, option, names, values):
        """
        coi_nai_seq
            : COI NAI
            | COI
            | coi_nai_seq COI NAI
            | coi_nai_seq COI
        """
        return self.defaultNodeClass(
            target="coi_nai_seq",
            option=option,
            names=names,
            values=values)

    def on_indicators(self, target, option, names, values):
        """
        indicators
            : FUhE indicator_seq
            | indicator_seq
        """
        return self.defaultNodeClass(
            target="indicators",
            option=option,
            names=names,
            values=values)

    def on_indicator_seq(self, target, option, names, values):
        """
        indicator_seq
            : indicator_seq indicator
            | indicator
        """
        return self.defaultNodeClass(
            target="indicator_seq",
            option=option,
            names=names,
            values=values)

    def on_indicator(self, target, option, names, values):
        """
        indicator
            : UI NAI
            | UI
            | CAI NAI
            | CAI
            | Y
            | DAhO
            | FUhO
        """
        return self.defaultNodeClass(
            target="indicator",
            option=option,
            names=names,
            values=values)

    def on_NAI_seq(self, target, option, names, values):
        """
        NAI_seq
            : NAI_seq NAI
            | NAI
        """
        return self.defaultNodeClass(
            target="NAI_seq",
            option=option,
            names=names,
            values=values)

    def on_CMENE_seq(self, target, option, names, values):
        """
        CMENE_seq
            : CMENE_seq CMENE
            | CMENE
        """
        return self.defaultNodeClass(
            target="CMENE_seq",
            option=option,
            names=names,
            values=values)

    def on_NIhO_seq_free_seq(self, target, option, names, values):
        """
        NIhO_seq_free_seq
            : NIhO_seq free_seq
            | NIhO_seq
        """
        return self.defaultNodeClass(
            target="NIhO_seq_free_seq",
            option=option,
            names=names,
            values=values)

    def on_NIhO_seq(self, target, option, names, values):
        """
        NIhO_seq
            : NIhO_seq NIhO
            | NIhO
        """
        return self.defaultNodeClass(
            target="NIhO_seq",
            option=option,
            names=names,
            values=values)

    # -----------------------------------------
    # raw lex script, verbatim here
    # -----------------------------------------
    lexscript = r"""
/***-*- Fundamental -*-************************************
  $Header$

  Functions for gathering text into a list and preprocessing the list.
  ***************************************/

/* COPYRIGHT */

%{
#include "cm.h"
static int pdepth = 0;
%}

C	[bcdfgjklmnprstvxz]
CNR	[bcdfgjklmnpstvxz]
V	[aeiou]
L	({C}|{V}|y|\')
LC  {L},?

/* The definition of cmavo is pretty liberal, allowing (hopefully)
   the minimum punctuation and arbitrary extensions, e.g. ca'ai'au. */
VV  {V}{V}?
VVY {VV}|y

CCC {C}{VVY}(\'{VVY})*
VCC {VVY}(\'{VVY})*

CMT ({CCC}|\.{VCC})*
CM1 {CCC}{CMT}
CM2 \.?{VCC}{CMT}
CM  {CM1}|{CM2}

/* These patterns are compelled to be BRIVLA - they are the special
   cases where r, n or y is inserted to prevent a cmavo breaking off. */
BM1 {C}{V}\'?{V}r{CNR}{L}+{V}
BM2 {C}{V}\'?{V}nr{L}+{V}
BM3 {C}{V}{C}y{C}{L}+{V}
BM  {BM1}|{BM2}|{BM3}

%x PAREN

/* The main rule for brivla is a pretty liberal definition - it should match
   fu'ivla too. Rely on the cmavo rule coming earlier so that sequences of
   cmavo glued together don't match this rule. */

%%

{BM}                { gather_brivla(yytext); }
{CM}                { gather_cmavo(yytext); }
{C}{L}+{V}          { gather_brivla(yytext); }
(\.?{LC}*{C})\.?    { gather_cmene(yytext); }
{L}+                { gather_fallthru(yytext); }
[ \t]+              { /* discard */ }
\r?\n               { /* discard */ }
\r?\n(\r?\n)+       { gather_newline(); }
[([]                { pdepth++; BEGIN PAREN; gather_paren(yytext); }

<PAREN>[[(]         { ++pdepth; gather_paren(yytext); }
<PAREN>[^][()]+     { gather_paren(yytext); }
<PAREN>[])]         { --pdepth; gather_paren(yytext); if (pdepth==0) { BEGIN INITIAL;} }

[a-zA-Z]+           { gather_fallthru(yytext); }
.                   { gather_fallthru(yytext); }


    """
    # -----------------------------------------
    # end raw lex script
    # -----------------------------------------

def usage():
    print "%s: PyBison parser derived from %s and %s" % (sys.argv[0], bisonFile, lexFile)
    print "Usage: %s [-k] [-v] [-d] [filename]" % sys.argv[0]
    print "  -k       Keep temporary files used in building parse engine lib"
    print "  -v       Enable verbose messages while parser is running"
    print "  -d       Enable garrulous debug messages from parser engine"
    print "  filename path of a file to parse, defaults to stdin"

def main(*args):
    """
    Unit-testing func
    """

    keepfiles = 0
    verbose = 0
    debug = 0
    filename = None

    for s in ["-h", "-help", "--h", "--help", "-?"]:
        if s in args:
            usage()
            sys.exit(0)

    if len(args) > 0:
        if "-k" in args:
            keepfiles = 1
            args.remove("-k")
        if "-v" in args:
            verbose = 1
            args.remove("-v")
        if "-d" in args:
            debug = 1
            args.remove("-d")
    if len(args) > 0:
        filename = args[0]

    p = Parser(verbose=verbose, keepfiles=keepfiles)
    tree = p.run(file=filename, debug=debug)
    return tree

if __name__ == "__main__":
    main(*(sys.argv[1:]))

