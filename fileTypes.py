from openers import OpenFuncs

simpleText = {
    '.0': OpenFuncs.open_txt,
    '.1ST': OpenFuncs.open_txt,
    '.600': OpenFuncs.open_txt,
    '.602': OpenFuncs.open_txt,
    '.ABW': OpenFuncs.open_txt,
    '.ACL': OpenFuncs.open_txt,
    '.AFP': OpenFuncs.open_txt,
    '.AMI': OpenFuncs.open_txt,
    '.Amigaguide': OpenFuncs.open_txt,
    '.ANS': OpenFuncs.open_txt,
    '.ASC': OpenFuncs.open_txt,
    '.AWW': OpenFuncs.open_txt,
    '.CCF': OpenFuncs.open_txt,
    '.CWK': OpenFuncs.open_txt,
    '.DBK': OpenFuncs.open_txt,
    '.DOC': OpenFuncs.open_txt,
    '.DOCM': OpenFuncs.open_txt,
    '.DOT': OpenFuncs.open_txt,
    '.DOTX': OpenFuncs.open_txt,
    '.EGT': OpenFuncs.open_txt,
    '.EPUB': OpenFuncs.open_txt,
    '.EZW': OpenFuncs.open_txt,
    '.FDX': OpenFuncs.open_txt,
    '.FTM': OpenFuncs.open_txt,
    '.FTX': OpenFuncs.open_txt,
    '.GDOC': OpenFuncs.open_txt,
    '.HWP': OpenFuncs.open_txt,
    '.HWPML': OpenFuncs.open_txt,
    '.LOG': OpenFuncs.open_txt,
    '.LWP': OpenFuncs.open_txt,
    '.MBP': OpenFuncs.open_txt,
    '.MD': OpenFuncs.open_txt,
    '.ME': OpenFuncs.open_txt,
    '.MCW': OpenFuncs.open_txt,
    '.NB': OpenFuncs.open_txt,
    '.NBP': OpenFuncs.open_txt,
    '.NEIS': OpenFuncs.open_txt,
    '.ODM': OpenFuncs.open_txt,
    '.OTT': OpenFuncs.open_txt,
    '.OMM': OpenFuncs.open_txt,
    '.PAGES': OpenFuncs.open_txt,
    '.PAP': OpenFuncs.open_txt,
    '.PDAX': OpenFuncs.open_txt,
    '.QUOX': OpenFuncs.open_txt,
    '.RTF': OpenFuncs.open_txt,
    '.RPT': OpenFuncs.open_txt,
    '.SDW': OpenFuncs.open_txt,
    '.SE': OpenFuncs.open_txt,
    '.STW': OpenFuncs.open_txt,
    '.Sxw': OpenFuncs.open_txt,
    '.TeX': OpenFuncs.open_txt,
    '.INFO': OpenFuncs.open_txt,
    '.Troff': OpenFuncs.open_txt,
    '.TXT': OpenFuncs.open_txt,
    '.UOF': OpenFuncs.open_txt,
    '.UOML': OpenFuncs.open_txt,
    '.VIA': OpenFuncs.open_txt,
    '.WPD': OpenFuncs.open_txt,
    '.WPS': OpenFuncs.open_txt,
    '.WPT': OpenFuncs.open_txt,
    '.WRD': OpenFuncs.open_txt,
    '.WRF': OpenFuncs.open_txt,
    '.WRI': OpenFuncs.open_txt,
    '.XPS': OpenFuncs.open_txt,
    '.AHK' : OpenFuncs.open_txt,
    '.APPLESCRIPT' : OpenFuncs.open_txt,
    '.AS' : OpenFuncs.open_txt,
    '.AU3' : OpenFuncs.open_txt,
    '.BAT' : OpenFuncs.open_txt,
    '.BAS' : OpenFuncs.open_txt,
    '.CLJS' : OpenFuncs.open_txt,
    '.CMD' : OpenFuncs.open_txt,
    '.Coffee' : OpenFuncs.open_txt,
    '.duino' : OpenFuncs.open_txt,
    '.EGG' : OpenFuncs.open_txt,
    '.ERB' : OpenFuncs.open_txt,
    '.HTA' : OpenFuncs.open_txt,
    '.IBI' : OpenFuncs.open_txt,
    '.ICI' : OpenFuncs.open_txt,
    '.IJS' : OpenFuncs.open_txt,
    '..ipynb' : OpenFuncs.open_txt,
    '.ITCL' : OpenFuncs.open_txt,
    '.JS' : OpenFuncs.open_txt,
    '.JSFL' : OpenFuncs.open_txt,
    '.LUA' : OpenFuncs.open_txt,
    '.M' : OpenFuncs.open_txt,
    '.MRC' : OpenFuncs.open_txt,
    '.NCF' : OpenFuncs.open_txt,
    '.NUC' : OpenFuncs.open_txt,
    '.NUD' : OpenFuncs.open_txt,
    '.NUT' : OpenFuncs.open_txt,
    '.PHP' : OpenFuncs.open_txt,
    '.PL' : OpenFuncs.open_txt,
    '.PM' : OpenFuncs.open_txt,
    '.PS1' : OpenFuncs.open_txt,
    '.PS1XML' : OpenFuncs.open_txt,
    '.PSC1' : OpenFuncs.open_txt,
    '.PSD1' : OpenFuncs.open_txt,
    '.PSM1' : OpenFuncs.open_txt,
    '.PY' : OpenFuncs.open_txt,
    '.PYC' : OpenFuncs.open_txt,
    '.PYO' : OpenFuncs.open_txt,
    '.R' : OpenFuncs.open_txt,
    '.RB' : OpenFuncs.open_txt,
    '.RDP' : OpenFuncs.open_txt,
    '.SCPT' : OpenFuncs.open_txt,
    '.SCPTD' : OpenFuncs.open_txt,
    '.SDL' : OpenFuncs.open_txt,
    '.SH' : OpenFuncs.open_txt,
    '.SYJS' : OpenFuncs.open_txt,
    '.SYPY' : OpenFuncs.open_txt,
    '.TCL' : OpenFuncs.open_txt,
    '.VBS' : OpenFuncs.open_txt,
    '.XPL' : OpenFuncs.open_txt,
    '.ebuild' : OpenFuncs.open_txt,
}

Openers = {
    '.csv': OpenFuncs.open_csv,
    '.tsv': OpenFuncs.open_csv,
    '.xml': OpenFuncs.open_xml,
    '.disco': OpenFuncs.open_xml,
    '.lnk': OpenFuncs.open_lnk,
    '.json': OpenFuncs.open_json,
    '.excel': OpenFuncs.open_excel,
    '.pdf': OpenFuncs.open_pdf,
    '.epub': OpenFuncs.open_epub,
    '.kdbx': OpenFuncs.open_kdbx,
    '.odt': OpenFuncs.open_odt,
    '.html': OpenFuncs.open_html,
    '.xhtml': OpenFuncs.open_html,
    '.wav': OpenFuncs.open_wav,
    '.au': OpenFuncs.open_au,
    '.aiff': OpenFuncs.open_aiff,
    '.aifc': OpenFuncs.open_aifc,
    '.gzip': OpenFuncs.open_gzip,
    '.zip': OpenFuncs.open_zip,
    '.tar': OpenFuncs.open_tar,
    '.p': OpenFuncs.open_p,
    '.netrx': OpenFuncs.open_netrx,
    '.plist': OpenFuncs.open_plist,
    '.ini': OpenFuncs.open_ini,
    '.sav': OpenFuncs.open_sav
}

Openers.update(simpleText)