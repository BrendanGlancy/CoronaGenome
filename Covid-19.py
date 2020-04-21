#!/usr/bin/env python
# coding: utf-8

# In[9]:


import zlib
len(zlib.compress(cc.encode("utf-8")))


# In[10]:


import lzma
lsc = lzma.compress(cc.encode("utf-8"))
len(lsc)


# In[11]:


# Coronavirus is not the flu
# Cornavirus is Sars


# In[12]:


cc


# In[9]:


len(cc)


# In[13]:


#START	ATG
#Asn or Asp / B	AAT, AAC; GAT, GAC
#Gln or Glu / Z	CAA, CAG; GAA, GAG
tt = """
Ala / A	GCT, GCC, GCA, GCG
Ile / I	ATT, ATC, ATA
Arg / R	CGT, CGC, CGA, CGG; AGA, AGG
Leu / L	CTT, CTC, CTA, CTG; TTA, TTG
Asn / N	AAT, AAC
Lys / K	AAA, AAG
Asp / D	GAT, GAC
Met / M	ATG
Phe / F	TTT, TTC
Cys / C	TGT, TGC
Pro / P	CCT, CCC, CCA, CCG
Gln / Q	CAA, CAG
Ser / S	TCT, TCC, TCA, TCG; AGT, AGC
Glu / E	GAA, GAG
Thr / T	ACT, ACC, ACA, ACG
Trp / W	TGG
Gly / G	GGT, GGC, GGA, GGG
Tyr / Y	TAT, TAC
His / H	CAT, CAC
Val / V	GTT, GTC, GTA, GTG
STOP	TAA, TGA, TAG
""".strip()
dec = {}
for t in tt.split("\n"):
    k,v = t.split("\x09")
    if '/' in k:
        k = k.split("/")[-1].strip()
    k = k.replace("STOP", "*")
    v = v.replace(",", "").replace(";", "").lower().split(" ")
    for vv in v:
        if vv in dec:
            print("dup", vv)
        dec[vv] = k
len(set(dec.values()))


# In[21]:


sars_v1 = """
MESLVLGVNEKTHVQLSLPVLQVRDVLVRGFGDSVEEALSEAREHLKNGTCGLVELEKGV
LPQLEQPYVFIKRSDALSTNHGHKVVELVAEMDGIQYGRSGITLGVLVPHVGETPIAYRN
VLLRKNGNKGAGGHSYGIDLKSYDLGDELGTDPIEDYEQNWNTKHGSGALRELTRELNGG
AVTRYVDNNFCGPDGYPLDCIKDFLARAGKSMCTLSEQLDYIESKRGVYCCRDHEHEIAW
FTERSDKSYEHQTPFEIKSAKKFDTFKGECPKFVFPLNSKVKVIQPRVEKKKTEGFMGRI
RSVYPVASPQECNNMHLSTLMKCNHCDEVSWQTCDFLKATCEHCGTENLVIEGPTTCGYL
PTNAVVKMPCPACQDPEIGPEHSVADYHNHSNIETRLRKGGRTRCFGGCVFAYVGCYNKR
AYWVPRASADIGSGHTGITGDNVETLNEDLLEILSRERVNINIVGDFHLNEEVAIILASF
SASTSAFIDTIKSLDYKSFKTIVESCGNYKVTKGKPVKGAWNIGQQRSVLTPLCGFPSQA
AGVIRSIFARTLDAANHSIPDLQRAAVTILDGISEQSLRLVDAMVYTSDLLTNSVIIMAY
VTGGLVQQTSQWLSNLLGTTVEKLRPIFEWIEAKLSAGVEFLKDAWEILKFLITGVFDIV
KGQIQVASDNIKDCVKCFIDVVNKALEMCIDQVTIAGAKLRSLNLGEVFIAQSKGLYRQC
IRGKEQLQLLMPLKAPKEVTFLEGDSHDTVLTSEEVVLKNGELEALETPVDSFTNGAIVG
TPVCVNGLMLLEIKDKEQYCALSPGLLATNNVFRLKGGAPIKGVTFGEDTVWEVQGYKNV
RITFELDERVDKVLNEKCSVYTVESGTEVTEFACVVAEAVVKTLQPVSDLLTNMGIDLDE
WSVATFYLFDDAGEENFSSRMYCSFYPPDEEEEDDAECEEEEIDETCEHEYGTEDDYQGL
PLEFGASAETVRVEEEEEEDWLDDTTEQSEIEPEPEPTPEEPVNQFTGYLKLTDNVAIKC
VDIVKEAQSANPMVIVNAANIHLKHGGGVAGALNKATNGAMQKESDDYIKLNGPLTVGGS
CLLSGHNLAKKCLHVVGPNLNAGEDIQLLKAAYENFNSQDILLAPLLSAGIFGAKPLQSL
QVCVQTVRTQVYIAVNDKALYEQVVMDYLDNLKPRVEAPKQEEPPNTEDSKTEEKSVVQK
PVDVKPKIKACIDEVTTTLEETKFLTNKLLLFADINGKLYHDSQNMLRGEDMSFLEKDAP
YMVGDVITSGDITCVVIPSKKAGGTTEMLSRALKKVPVDEYITTYPGQGCAGYTLEEAKT
ALKKCKSAFYVLPSEAPNAKEEILGTVSWNLREMLAHAEETRKLMPICMDVRAIMATIQR
KYKGIKIQEGIVDYGVRFFFYTSKEPVASIITKLNSLNEPLVTMPIGYVTHGFNLEEAAR
CMRSLKAPAVVSVSSPDAVTTYNGYLTSSSKTSEEHFVETVSLAGSYRDWSYSGQRTELG
VEFLKRGDKIVYHTLESPVEFHLDGEVLSLDKLKSLLSLREVKTIKVFTTVDNTNLHTQL
VDMSMTYGQQFGPTYLDGADVTKIKPHVNHEGKTFFVLPSDDTLRSEAFEYYHTLDESFL
GRYMSALNHTKKWKFPQVGGLTSIKWADNNCYLSSVLLALQQLEVKFNAPALQEAYYRAR
AGDAANFCALILAYSNKTVGELGDVRETMTHLLQHANLESAKRVLNVVCKHCGQKTTTLT
GVEAVMYMGTLSYDNLKTGVSIPCVCGRDATQYLVQQESSFVMMSAPPAEYKLQQGTFLC
ANEYTGNYQCGHYTHITAKETLYRIDGAHLTKMSEYKGPVTDVFYKETSYTTTIKPVSYK
LDGVTYTEIEPKLDGYYKKDNAYYTEQPIDLVPTQPLPNASFDNFKLTCSNTKFADDLNQ
MTGFTKPASRELSVTFFPDLNGDVVAIDYRHYSASFKKGAKLLHKPIVWHINQATTKTTF
KPNTWCLRCLWSTKPVDTSNSFEVLAVEDTQGMDNLACESQQPTSEEVVENPTIQKEVIE
CDVKTTEVVGNVILKPSDEGVKVTQELGHEDLMAAYVENTSITIKKPNELSLALGLKTIA
THGIAAINSVPWSKILAYVKPFLGQAAITTSNCAKRLAQRVFNNYMPYVFTLLFQLCTFT
KSTNSRIRASLPTTIAKNSVKSVAKLCLDAGINYVKSPKFSKLFTIAMWLLLLSICLGSL
ICVTAAFGVLLSNFGAPSYCNGVRELYLNSSNVTTMDFCEGSFPCSICLSGLDSLDSYPA
LETIQVTISSYKLDLTILGLAAEWVLAYMLFTKFFYLLGLSAIMQVFFGYFASHFISNSW
LMWFIISIVQMAPVSAMVRMYIFFASFYYIWKSYVHIMDGCTSSTCMMCYKRNRATRVEC
TTIVNGMKRSFYVYANGGRGFCKTHNWNCLNCDTFCTGSTFISDEVARDLSLQFKRPINP
TDQSSYIVDSVAVKNGALHLYFDKAGQKTYERHPLSHFVNLDNLRANNTKGSLPINVIVF
DGKSKCDESASKSASVYYSQLMCQPILLLDQALVSDVGDSTEVSVKMFDAYVDTFSATFS
VPMEKLKALVATAHSELAKGVALDGVLSTFVSAARQGVVDTDVDTKDVIECLKLSHHSDL
EVTGDSCNNFMLTYNKVENMTPRDLGACIDCNARHINAQVAKSHNVSLIWNVKDYMSLSE
QLRKQIRSAAKKNNIPFRLTCATTRQVVNVITTKISLKGGKIVSTCFKLMLKATLLCVLA
ALVCYIVMPVHTLSIHDGYTNEIIGYKAIQDGVTRDIISTDDCFANKHAGFDAWFSQRGG
SYKNDKSCPVVAAIITREIGFIVPGLPGTVLRAINGDFLHFLPRVFSAVGNICYTPSKLI
EYSDFATSACVLAAECTIFKDAMGKPVPYCYDTNLLEGSISYSELRPDTRYVLMDGSIIQ
FPNTYLEGSVRVVTTFDAEYCRHGTCERSEVGICLSTSGRWVLNNEHYRALSGVFCGVDA
MNLIANIFTPLVQPVGALDVSASVVAGGIIAILVTCAAYYFMKFRRVFGEYNHVVAANAL
LFLMSFTILCLVPAYSFLPGVYSVFYLYLTFYFTNDVSFLAHLQWFAMFSPIVPFWITAI
YVFCISLKHCHWFFNNYLRKRVMFNGVTFSTFEEAALCTFLLNKEMYLKLRSETLLPLTQ
YNRYLALYNKYKYFSGALDTTSYREAACCHLAKALNDFSNSGADVLYQPPQTSITSAVLQ
SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIR
KSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNG
SPSGVYQCAMRPNHTIKGSFLNGSCGSVGFNIDYDCVSFCYMHHMELPTGVHAGTDLEGK
FYGPFVDRQTAQAAGTDTTITLNVLAWLYAAVINGDRWFLNRFTTTLNDFNLVAMKYNYE
PLTQDHVDILGPLSAQTGIAVLDMCAALKELLQNGMNGRTILGSTILEDEFTPFDVVRQC
SGVTFQGKFKKIVKGTHHWMLLTFLTSLLILVQSTQWSLFFFVYENAFLPFTLGIMAIAA
CAMLLVKHKHAFLCLFLLPSLATVAYFNMVYMPASWVMRIMTWLELADTSLSGYRLKDCV
MYASALVLLILMTARTVYDDAARRVWTLMNVITLVYKVYYGNALDQAISMWALVISVTSN
YSGVVTTIMFLARAIVFVCVEYYPLLFITGNTLQCIMLVYCFLGYCCCCYFGLFCLLNRY
FRLTLGVYDYLVSTQEFRYMNSQGLLPPKSSIDAFKLNIKLLGIGGKPCIKVATVQSKMS
DVKCTSVVLLSVLQQLRVESSSKLWAQCVQLHNDILLAKDTTEAFEKMVSLLSVLLSMQG
AVDINRLCEEMLDNRATLQAIASEFSSLPSYAAYATAQEAYEQAVANGDSEVVLKKLKKS
LNVAKSEFDRDAAMQRKLEKMADQAMTQMYKQARSEDKRAKVTSAMQTMLFTMLRKLDND
ALNNIINNARDGCVPLNIIPLTTAAKLMVVVPDYGTYKNTCDGNTFTYASALWEIQQVVD
ADSKIVQLSEINMDNSPNLAWPLIVTALRANSAVKLQNNELSPVALRQMSCAAGTTQTAC
TDDNALAYYNNSKGGRFVLALLSDHQDLKWARFPKSDGTGTIYTELEPPCRFVTDTPKGP
KVKYLYFIKGLNNLNRGMVLGSLAATVRLQAGNATEVPANSTVLSFCAFAVDPAKAYKDY
LASGGQPITNCVKMLCTHTGTGQAITVTPEANMDQESFGGASCCLYCRCHIDHPNPKGFC
DLKGKYVQIPTTCANDPVGFTLRNTVCTVCGMWKGYGCSCDQLREPLMQSADASTFLNGF
AV""".replace("\n","")


# In[48]:


sars_v1


# In[49]:


sars_v2 = decode(cc[266-1:13483])


# In[3]:


from Bio import GenBank
gi_list = GenBank.search_for("sars")


# In[1]:


import nglview
view = nglview.show_pdbid("5re4")  # load "3pqr" from RCSB PDB and display viewer widget
view


# In[ ]:


#https://www.ncbi.nlm.nih.gov/nuccore/NC_045512 - complete genome

# Copies the virus
orf1a = translate(cc[266-1:13483], True)
orf1b = translate(cc[13468-1:21555], False)

# Sticks to Ace2, exploit vector 
spike_glycoprotein = translate(cc[21563-1:25384], True)

orf3a = translate(cc[25393-1:26220], True)

enevolpe_protein = translate(cc[26245-1:26472], True)
membrane_protein = translate(cc[26523-1:27191], True)

orf6 = translate(cc[27202-1:27387], True)
orf7a = translate(cc[27394-1:27759], True)
orf7b = translate(cc[27756-1:27887], True)
orf8 = translate(cc[27894-1:28259], True)
orf9 = translate(cc[28274-1:29533], True)


# In[82]:


cn3 = open("/Users/brendang/Downloads/mmdb_6VSB.cn3", "rb").read()


# In[69]:


# "orf1a polyprotein" = https://www.ncbi.nlm.nih.gov/protein/1802476803
# usage (orf1ab, is sars_v1) = https://www.uniprot.org/uniprot/Q0ZJN1


# "Spike glycoprotein" 
sars_v2 = translation(cc[266-1:13483], True)
orf1b = translation(cc[13468-1:21555], False)
print(orf1b)
spike_glycoprotein = translation(cc[21563-1:25384], True)
#print(len(sars_v1), len(sars_v2), len(spike_glycoprotein))

#len(lzma.compress(spike_glycoprotein.encode("utf-8")))
# https://www.ncbi.nlm.nih.gov/Structure/pdb/6VXX -- closed state?
# https://www.ncbi.nlm.nih.gov/Structure/pdb/6VYB -- open state?
spike_glycoprotein


# In[15]:


def translate(x, protein=False):
    aa = []
    for i in range(0, len(x)-2, 3):
        aa.append(dec[x[i:i+3]])
    aa = ''.join(aa)
    if protein:
        if aa[0] != "M" or aa[-1] != "*":
            print("BAD PROTEIN")
            print(aa)
            return None
        aa = aa[:-1]
    return aa
aa = translate(cc[0:]) + translate(cc[1:]) + translate(cc[2:])


# In[8]:


cc = """
1 attaaaggtt tataccttcc caggtaacaa accaaccaac tttcgatctc ttgtagatct
       61 gttctctaaa cgaactttaa aatctgtgtg gctgtcactc ggctgcatgc ttagtgcact
      121 cacgcagtat aattaataac taattactgt cgttgacagg acacgagtaa ctcgtctatc
      181 ttctgcaggc tgcttacggt ttcgtccgtg ttgcagccga tcatcagcac atctaggttt
      241 cgtccgggtg tgaccgaaag gtaagatgga gagccttgtc cctggtttca acgagaaaac
      301 acacgtccaa ctcagtttgc ctgttttaca ggttcgcgac gtgctcgtac gtggctttgg
      361 agactccgtg gaggaggtct tatcagaggc acgtcaacat cttaaagatg gcacttgtgg
      421 cttagtagaa gttgaaaaag gcgttttgcc tcaacttgaa cagccctatg tgttcatcaa
      481 acgttcggat gctcgaactg cacctcatgg tcatgttatg gttgagctgg tagcagaact
      541 cgaaggcatt cagtacggtc gtagtggtga gacacttggt gtccttgtcc ctcatgtggg
      601 cgaaatacca gtggcttacc gcaaggttct tcttcgtaag aacggtaata aaggagctgg
      661 tggccatagt tacggcgccg atctaaagtc atttgactta ggcgacgagc ttggcactga
      721 tccttatgaa gattttcaag aaaactggaa cactaaacat agcagtggtg ttacccgtga
      781 actcatgcgt gagcttaacg gaggggcata cactcgctat gtcgataaca acttctgtgg
      841 ccctgatggc taccctcttg agtgcattaa agaccttcta gcacgtgctg gtaaagcttc
      901 atgcactttg tccgaacaac tggactttat tgacactaag aggggtgtat actgctgccg
      961 tgaacatgag catgaaattg cttggtacac ggaacgttct gaaaagagct atgaattgca
     1021 gacacctttt gaaattaaat tggcaaagaa atttgacacc ttcaatgggg aatgtccaaa
     1081 ttttgtattt cccttaaatt ccataatcaa gactattcaa ccaagggttg aaaagaaaaa
     1141 gcttgatggc tttatgggta gaattcgatc tgtctatcca gttgcgtcac caaatgaatg
     1201 caaccaaatg tgcctttcaa ctctcatgaa gtgtgatcat tgtggtgaaa cttcatggca
     1261 gacgggcgat tttgttaaag ccacttgcga attttgtggc actgagaatt tgactaaaga
     1321 aggtgccact acttgtggtt acttacccca aaatgctgtt gttaaaattt attgtccagc
     1381 atgtcacaat tcagaagtag gacctgagca tagtcttgcc gaataccata atgaatctgg
     1441 cttgaaaacc attcttcgta agggtggtcg cactattgcc tttggaggct gtgtgttctc
     1501 ttatgttggt tgccataaca agtgtgccta ttgggttcca cgtgctagcg ctaacatagg
     1561 ttgtaaccat acaggtgttg ttggagaagg ttccgaaggt cttaatgaca accttcttga
     1621 aatactccaa aaagagaaag tcaacatcaa tattgttggt gactttaaac ttaatgaaga
     1681 gatcgccatt attttggcat ctttttctgc ttccacaagt gcttttgtgg aaactgtgaa
     1741 aggtttggat tataaagcat tcaaacaaat tgttgaatcc tgtggtaatt ttaaagttac
     1801 aaaaggaaaa gctaaaaaag gtgcctggaa tattggtgaa cagaaatcaa tactgagtcc
     1861 tctttatgca tttgcatcag aggctgctcg tgttgtacga tcaattttct cccgcactct
     1921 tgaaactgct caaaattctg tgcgtgtttt acagaaggcc gctataacaa tactagatgg
     1981 aatttcacag tattcactga gactcattga tgctatgatg ttcacatctg atttggctac
     2041 taacaatcta gttgtaatgg cctacattac aggtggtgtt gttcagttga cttcgcagtg
     2101 gctaactaac atctttggca ctgtttatga aaaactcaaa cccgtccttg attggcttga
     2161 agagaagttt aaggaaggtg tagagtttct tagagacggt tgggaaattg ttaaatttat
     2221 ctcaacctgt gcttgtgaaa ttgtcggtgg acaaattgtc acctgtgcaa aggaaattaa
     2281 ggagagtgtt cagacattct ttaagcttgt aaataaattt ttggctttgt gtgctgactc
     2341 tatcattatt ggtggagcta aacttaaagc cttgaattta ggtgaaacat ttgtcacgca
     2401 ctcaaaggga ttgtacagaa agtgtgttaa atccagagaa gaaactggcc tactcatgcc
     2461 tctaaaagcc ccaaaagaaa ttatcttctt agagggagaa acacttccca cagaagtgtt
     2521 aacagaggaa gttgtcttga aaactggtga tttacaacca ttagaacaac ctactagtga
     2581 agctgttgaa gctccattgg ttggtacacc agtttgtatt aacgggctta tgttgctcga
     2641 aatcaaagac acagaaaagt actgtgccct tgcacctaat atgatggtaa caaacaatac
     2701 cttcacactc aaaggcggtg caccaacaaa ggttactttt ggtgatgaca ctgtgataga
     2761 agtgcaaggt tacaagagtg tgaatatcac ttttgaactt gatgaaagga ttgataaagt
     2821 acttaatgag aagtgctctg cctatacagt tgaactcggt acagaagtaa atgagttcgc
     2881 ctgtgttgtg gcagatgctg tcataaaaac tttgcaacca gtatctgaat tacttacacc
     2941 actgggcatt gatttagatg agtggagtat ggctacatac tacttatttg atgagtctgg
     3001 tgagtttaaa ttggcttcac atatgtattg ttctttctac cctccagatg aggatgaaga
     3061 agaaggtgat tgtgaagaag aagagtttga gccatcaact caatatgagt atggtactga
     3121 agatgattac caaggtaaac ctttggaatt tggtgccact tctgctgctc ttcaacctga
     3181 agaagagcaa gaagaagatt ggttagatga tgatagtcaa caaactgttg gtcaacaaga
     3241 cggcagtgag gacaatcaga caactactat tcaaacaatt gttgaggttc aacctcaatt
     3301 agagatggaa cttacaccag ttgttcagac tattgaagtg aatagtttta gtggttattt
     3361 aaaacttact gacaatgtat acattaaaaa tgcagacatt gtggaagaag ctaaaaaggt
     3421 aaaaccaaca gtggttgtta atgcagccaa tgtttacctt aaacatggag gaggtgttgc
     3481 aggagcctta aataaggcta ctaacaatgc catgcaagtt gaatctgatg attacatagc
     3541 tactaatgga ccacttaaag tgggtggtag ttgtgtttta agcggacaca atcttgctaa
     3601 acactgtctt catgttgtcg gcccaaatgt taacaaaggt gaagacattc aacttcttaa
     3661 gagtgcttat gaaaatttta atcagcacga agttctactt gcaccattat tatcagctgg
     3721 tatttttggt gctgacccta tacattcttt aagagtttgt gtagatactg ttcgcacaaa
     3781 tgtctactta gctgtctttg ataaaaatct ctatgacaaa cttgtttcaa gctttttgga
     3841 aatgaagagt gaaaagcaag ttgaacaaaa gatcgctgag attcctaaag aggaagttaa
     3901 gccatttata actgaaagta aaccttcagt tgaacagaga aaacaagatg ataagaaaat
     3961 caaagcttgt gttgaagaag ttacaacaac tctggaagaa actaagttcc tcacagaaaa
     4021 cttgttactt tatattgaca ttaatggcaa tcttcatcca gattctgcca ctcttgttag
     4081 tgacattgac atcactttct taaagaaaga tgctccatat atagtgggtg atgttgttca
     4141 agagggtgtt ttaactgctg tggttatacc tactaaaaag gctggtggca ctactgaaat
     4201 gctagcgaaa gctttgagaa aagtgccaac agacaattat ataaccactt acccgggtca
     4261 gggtttaaat ggttacactg tagaggaggc aaagacagtg cttaaaaagt gtaaaagtgc
     4321 cttttacatt ctaccatcta ttatctctaa tgagaagcaa gaaattcttg gaactgtttc
     4381 ttggaatttg cgagaaatgc ttgcacatgc agaagaaaca cgcaaattaa tgcctgtctg
     4441 tgtggaaact aaagccatag tttcaactat acagcgtaaa tataagggta ttaaaataca
     4501 agagggtgtg gttgattatg gtgctagatt ttacttttac accagtaaaa caactgtagc
     4561 gtcacttatc aacacactta acgatctaaa tgaaactctt gttacaatgc cacttggcta
     4621 tgtaacacat ggcttaaatt tggaagaagc tgctcggtat atgagatctc tcaaagtgcc
     4681 agctacagtt tctgtttctt cacctgatgc tgttacagcg tataatggtt atcttacttc
     4741 ttcttctaaa acacctgaag aacattttat tgaaaccatc tcacttgctg gttcctataa
     4801 agattggtcc tattctggac aatctacaca actaggtata gaatttctta agagaggtga
     4861 taaaagtgta tattacacta gtaatcctac cacattccac ctagatggtg aagttatcac
     4921 ctttgacaat cttaagacac ttctttcttt gagagaagtg aggactatta aggtgtttac
     4981 aacagtagac aacattaacc tccacacgca agttgtggac atgtcaatga catatggaca
     5041 acagtttggt ccaacttatt tggatggagc tgatgttact aaaataaaac ctcataattc
     5101 acatgaaggt aaaacatttt atgttttacc taatgatgac actctacgtg ttgaggcttt
     5161 tgagtactac cacacaactg atcctagttt tctgggtagg tacatgtcag cattaaatca
     5221 cactaaaaag tggaaatacc cacaagttaa tggtttaact tctattaaat gggcagataa
     5281 caactgttat cttgccactg cattgttaac actccaacaa atagagttga agtttaatcc
     5341 acctgctcta caagatgctt attacagagc aagggctggt gaagctgcta acttttgtgc
     5401 acttatctta gcctactgta ataagacagt aggtgagtta ggtgatgtta gagaaacaat
     5461 gagttacttg tttcaacatg ccaatttaga ttcttgcaaa agagtcttga acgtggtgtg
     5521 taaaacttgt ggacaacagc agacaaccct taagggtgta gaagctgtta tgtacatggg
     5581 cacactttct tatgaacaat ttaagaaagg tgttcagata ccttgtacgt gtggtaaaca
     5641 agctacaaaa tatctagtac aacaggagtc accttttgtt atgatgtcag caccacctgc
     5701 tcagtatgaa cttaagcatg gtacatttac ttgtgctagt gagtacactg gtaattacca
     5761 gtgtggtcac tataaacata taacttctaa agaaactttg tattgcatag acggtgcttt
     5821 acttacaaag tcctcagaat acaaaggtcc tattacggat gttttctaca aagaaaacag
     5881 ttacacaaca accataaaac cagttactta taaattggat ggtgttgttt gtacagaaat
     5941 tgaccctaag ttggacaatt attataagaa agacaattct tatttcacag agcaaccaat
     6001 tgatcttgta ccaaaccaac catatccaaa cgcaagcttc gataatttta agtttgtatg
     6061 tgataatatc aaatttgctg atgatttaaa ccagttaact ggttataaga aacctgcttc
     6121 aagagagctt aaagttacat ttttccctga cttaaatggt gatgtggtgg ctattgatta
     6181 taaacactac acaccctctt ttaagaaagg agctaaattg ttacataaac ctattgtttg
     6241 gcatgttaac aatgcaacta ataaagccac gtataaacca aatacctggt gtatacgttg
     6301 tctttggagc acaaaaccag ttgaaacatc aaattcgttt gatgtactga agtcagagga
     6361 cgcgcaggga atggataatc ttgcctgcga agatctaaaa ccagtctctg aagaagtagt
     6421 ggaaaatcct accatacaga aagacgttct tgagtgtaat gtgaaaacta ccgaagttgt
     6481 aggagacatt atacttaaac cagcaaataa tagtttaaaa attacagaag aggttggcca
     6541 cacagatcta atggctgctt atgtagacaa ttctagtctt actattaaga aacctaatga
     6601 attatctaga gtattaggtt tgaaaaccct tgctactcat ggtttagctg ctgttaatag
     6661 tgtcccttgg gatactatag ctaattatgc taagcctttt cttaacaaag ttgttagtac
     6721 aactactaac atagttacac ggtgtttaaa ccgtgtttgt actaattata tgccttattt
     6781 ctttacttta ttgctacaat tgtgtacttt tactagaagt acaaattcta gaattaaagc
     6841 atctatgccg actactatag caaagaatac tgttaagagt gtcggtaaat tttgtctaga
     6901 ggcttcattt aattatttga agtcacctaa tttttctaaa ctgataaata ttataatttg
     6961 gtttttacta ttaagtgttt gcctaggttc tttaatctac tcaaccgctg ctttaggtgt
     7021 tttaatgtct aatttaggca tgccttctta ctgtactggt tacagagaag gctatttgaa
     7081 ctctactaat gtcactattg caacctactg tactggttct ataccttgta gtgtttgtct
     7141 tagtggttta gattctttag acacctatcc ttctttagaa actatacaaa ttaccatttc
     7201 atcttttaaa tgggatttaa ctgcttttgg cttagttgca gagtggtttt tggcatatat
     7261 tcttttcact aggtttttct atgtacttgg attggctgca atcatgcaat tgtttttcag
     7321 ctattttgca gtacatttta ttagtaattc ttggcttatg tggttaataa ttaatcttgt
     7381 acaaatggcc ccgatttcag ctatggttag aatgtacatc ttctttgcat cattttatta
     7441 tgtatggaaa agttatgtgc atgttgtaga cggttgtaat tcatcaactt gtatgatgtg
     7501 ttacaaacgt aatagagcaa caagagtcga atgtacaact attgttaatg gtgttagaag
     7561 gtccttttat gtctatgcta atggaggtaa aggcttttgc aaactacaca attggaattg
     7621 tgttaattgt gatacattct gtgctggtag tacatttatt agtgatgaag ttgcgagaga
     7681 cttgtcacta cagtttaaaa gaccaataaa tcctactgac cagtcttctt acatcgttga
     7741 tagtgttaca gtgaagaatg gttccatcca tctttacttt gataaagctg gtcaaaagac
     7801 ttatgaaaga cattctctct ctcattttgt taacttagac aacctgagag ctaataacac
     7861 taaaggttca ttgcctatta atgttatagt ttttgatggt aaatcaaaat gtgaagaatc
     7921 atctgcaaaa tcagcgtctg tttactacag tcagcttatg tgtcaaccta tactgttact
     7981 agatcaggca ttagtgtctg atgttggtga tagtgcggaa gttgcagtta aaatgtttga
     8041 tgcttacgtt aatacgtttt catcaacttt taacgtacca atggaaaaac tcaaaacact
     8101 agttgcaact gcagaagctg aacttgcaaa gaatgtgtcc ttagacaatg tcttatctac
     8161 ttttatttca gcagctcggc aagggtttgt tgattcagat gtagaaacta aagatgttgt
     8221 tgaatgtctt aaattgtcac atcaatctga catagaagtt actggcgata gttgtaataa
     8281 ctatatgctc acctataaca aagttgaaaa catgacaccc cgtgaccttg gtgcttgtat
     8341 tgactgtagt gcgcgtcata ttaatgcgca ggtagcaaaa agtcacaaca ttgctttgat
     8401 atggaacgtt aaagatttca tgtcattgtc tgaacaacta cgaaaacaaa tacgtagtgc
     8461 tgctaaaaag aataacttac cttttaagtt gacatgtgca actactagac aagttgttaa
     8521 tgttgtaaca acaaagatag cacttaaggg tggtaaaatt gttaataatt ggttgaagca
     8581 gttaattaaa gttacacttg tgttcctttt tgttgctgct attttctatt taataacacc
     8641 tgttcatgtc atgtctaaac atactgactt ttcaagtgaa atcataggat acaaggctat
     8701 tgatggtggt gtcactcgtg acatagcatc tacagatact tgttttgcta acaaacatgc
     8761 tgattttgac acatggttta gccagcgtgg tggtagttat actaatgaca aagcttgccc
     8821 attgattgct gcagtcataa caagagaagt gggttttgtc gtgcctggtt tgcctggcac
     8881 gatattacgc acaactaatg gtgacttttt gcatttctta cctagagttt ttagtgcagt
     8941 tggtaacatc tgttacacac catcaaaact tatagagtac actgactttg caacatcagc
     9001 ttgtgttttg gctgctgaat gtacaatttt taaagatgct tctggtaagc cagtaccata
     9061 ttgttatgat accaatgtac tagaaggttc tgttgcttat gaaagtttac gccctgacac
     9121 acgttatgtg ctcatggatg gctctattat tcaatttcct aacacctacc ttgaaggttc
     9181 tgttagagtg gtaacaactt ttgattctga gtactgtagg cacggcactt gtgaaagatc
     9241 agaagctggt gtttgtgtat ctactagtgg tagatgggta cttaacaatg attattacag
     9301 atctttacca ggagttttct gtggtgtaga tgctgtaaat ttacttacta atatgtttac
     9361 accactaatt caacctattg gtgctttgga catatcagca tctatagtag ctggtggtat
     9421 tgtagctatc gtagtaacat gccttgccta ctattttatg aggtttagaa gagcttttgg
     9481 tgaatacagt catgtagttg cctttaatac tttactattc cttatgtcat tcactgtact
     9541 ctgtttaaca ccagtttact cattcttacc tggtgtttat tctgttattt acttgtactt
     9601 gacattttat cttactaatg atgtttcttt tttagcacat attcagtgga tggttatgtt
     9661 cacaccttta gtacctttct ggataacaat tgcttatatc atttgtattt ccacaaagca
     9721 tttctattgg ttctttagta attacctaaa gagacgtgta gtctttaatg gtgtttcctt
     9781 tagtactttt gaagaagctg cgctgtgcac ctttttgtta aataaagaaa tgtatctaaa
     9841 gttgcgtagt gatgtgctat tacctcttac gcaatataat agatacttag ctctttataa
     9901 taagtacaag tattttagtg gagcaatgga tacaactagc tacagagaag ctgcttgttg
     9961 tcatctcgca aaggctctca atgacttcag taactcaggt tctgatgttc tttaccaacc
    10021 accacaaacc tctatcacct cagctgtttt gcagagtggt tttagaaaaa tggcattccc
    10081 atctggtaaa gttgagggtt gtatggtaca agtaacttgt ggtacaacta cacttaacgg
    10141 tctttggctt gatgacgtag tttactgtcc aagacatgtg atctgcacct ctgaagacat
    10201 gcttaaccct aattatgaag atttactcat tcgtaagtct aatcataatt tcttggtaca
    10261 ggctggtaat gttcaactca gggttattgg acattctatg caaaattgtg tacttaagct
    10321 taaggttgat acagccaatc ctaagacacc taagtataag tttgttcgca ttcaaccagg
    10381 acagactttt tcagtgttag cttgttacaa tggttcacca tctggtgttt accaatgtgc
    10441 tatgaggccc aatttcacta ttaagggttc attccttaat ggttcatgtg gtagtgttgg
    10501 ttttaacata gattatgact gtgtctcttt ttgttacatg caccatatgg aattaccaac
    10561 tggagttcat gctggcacag acttagaagg taacttttat ggaccttttg ttgacaggca
    10621 aacagcacaa gcagctggta cggacacaac tattacagtt aatgttttag cttggttgta
    10681 cgctgctgtt ataaatggag acaggtggtt tctcaatcga tttaccacaa ctcttaatga
    10741 ctttaacctt gtggctatga agtacaatta tgaacctcta acacaagacc atgttgacat
    10801 actaggacct ctttctgctc aaactggaat tgccgtttta gatatgtgtg cttcattaaa
    10861 agaattactg caaaatggta tgaatggacg taccatattg ggtagtgctt tattagaaga
    10921 tgaatttaca ccttttgatg ttgttagaca atgctcaggt gttactttcc aaagtgcagt
    10981 gaaaagaaca atcaagggta cacaccactg gttgttactc acaattttga cttcactttt
    11041 agttttagtc cagagtactc aatggtcttt gttctttttt ttgtatgaaa atgccttttt
    11101 accttttgct atgggtatta ttgctatgtc tgcttttgca atgatgtttg tcaaacataa
    11161 gcatgcattt ctctgtttgt ttttgttacc ttctcttgcc actgtagctt attttaatat
    11221 ggtctatatg cctgctagtt gggtgatgcg tattatgaca tggttggata tggttgatac
    11281 tagtttgtct ggttttaagc taaaagactg tgttatgtat gcatcagctg tagtgttact
    11341 aatccttatg acagcaagaa ctgtgtatga tgatggtgct aggagagtgt ggacacttat
    11401 gaatgtcttg acactcgttt ataaagttta ttatggtaat gctttagatc aagccatttc
    11461 catgtgggct cttataatct ctgttacttc taactactca ggtgtagtta caactgtcat
    11521 gtttttggcc agaggtattg tttttatgtg tgttgagtat tgccctattt tcttcataac
    11581 tggtaataca cttcagtgta taatgctagt ttattgtttc ttaggctatt tttgtacttg
    11641 ttactttggc ctcttttgtt tactcaaccg ctactttaga ctgactcttg gtgtttatga
    11701 ttacttagtt tctacacagg agtttagata tatgaattca cagggactac tcccacccaa
    11761 gaatagcata gatgccttca aactcaacat taaattgttg ggtgttggtg gcaaaccttg
    11821 tatcaaagta gccactgtac agtctaaaat gtcagatgta aagtgcacat cagtagtctt
    11881 actctcagtt ttgcaacaac tcagagtaga atcatcatct aaattgtggg ctcaatgtgt
    11941 ccagttacac aatgacattc tcttagctaa agatactact gaagcctttg aaaaaatggt
    12001 ttcactactt tctgttttgc tttccatgca gggtgctgta gacataaaca agctttgtga
    12061 agaaatgctg gacaacaggg caaccttaca agctatagcc tcagagttta gttcccttcc
    12121 atcatatgca gcttttgcta ctgctcaaga agcttatgag caggctgttg ctaatggtga
    12181 ttctgaagtt gttcttaaaa agttgaagaa gtctttgaat gtggctaaat ctgaatttga
    12241 ccgtgatgca gccatgcaac gtaagttgga aaagatggct gatcaagcta tgacccaaat
    12301 gtataaacag gctagatctg aggacaagag ggcaaaagtt actagtgcta tgcagacaat
    12361 gcttttcact atgcttagaa agttggataa tgatgcactc aacaacatta tcaacaatgc
    12421 aagagatggt tgtgttccct tgaacataat acctcttaca acagcagcca aactaatggt
    12481 tgtcatacca gactataaca catataaaaa tacgtgtgat ggtacaacat ttacttatgc
    12541 atcagcattg tgggaaatcc aacaggttgt agatgcagat agtaaaattg ttcaacttag
    12601 tgaaattagt atggacaatt cacctaattt agcatggcct cttattgtaa cagctttaag
    12661 ggccaattct gctgtcaaat tacagaataa tgagcttagt cctgttgcac tacgacagat
    12721 gtcttgtgct gccggtacta cacaaactgc ttgcactgat gacaatgcgt tagcttacta
    12781 caacacaaca aagggaggta ggtttgtact tgcactgtta tccgatttac aggatttgaa
    12841 atgggctaga ttccctaaga gtgatggaac tggtactatc tatacagaac tggaaccacc
    12901 ttgtaggttt gttacagaca cacctaaagg tcctaaagtg aagtatttat actttattaa
    12961 aggattaaac aacctaaata gaggtatggt acttggtagt ttagctgcca cagtacgtct
    13021 acaagctggt aatgcaacag aagtgcctgc caattcaact gtattatctt tctgtgcttt
    13081 tgctgtagat gctgctaaag cttacaaaga ttatctagct agtgggggac aaccaatcac
    13141 taattgtgtt aagatgttgt gtacacacac tggtactggt caggcaataa cagttacacc
    13201 ggaagccaat atggatcaag aatcctttgg tggtgcatcg tgttgtctgt actgccgttg
    13261 ccacatagat catccaaatc ctaaaggatt ttgtgactta aaaggtaagt atgtacaaat
    13321 acctacaact tgtgctaatg accctgtggg ttttacactt aaaaacacag tctgtaccgt
    13381 ctgcggtatg tggaaaggtt atggctgtag ttgtgatcaa ctccgcgaac ccatgcttca
    13441 gtcagctgat gcacaatcgt ttttaaacgg gtttgcggtg taagtgcagc ccgtcttaca
    13501 ccgtgcggca caggcactag tactgatgtc gtatacaggg cttttgacat ctacaatgat
    13561 aaagtagctg gttttgctaa attcctaaaa actaattgtt gtcgcttcca agaaaaggac
    13621 gaagatgaca atttaattga ttcttacttt gtagttaaga gacacacttt ctctaactac
    13681 caacatgaag aaacaattta taatttactt aaggattgtc cagctgttgc taaacatgac
    13741 ttctttaagt ttagaataga cggtgacatg gtaccacata tatcacgtca acgtcttact
    13801 aaatacacaa tggcagacct cgtctatgct ttaaggcatt ttgatgaagg taattgtgac
    13861 acattaaaag aaatacttgt cacatacaat tgttgtgatg atgattattt caataaaaag
    13921 gactggtatg attttgtaga aaacccagat atattacgcg tatacgccaa cttaggtgaa
    13981 cgtgtacgcc aagctttgtt aaaaacagta caattctgtg atgccatgcg aaatgctggt
    14041 attgttggtg tactgacatt agataatcaa gatctcaatg gtaactggta tgatttcggt
    14101 gatttcatac aaaccacgcc aggtagtgga gttcctgttg tagattctta ttattcattg
    14161 ttaatgccta tattaacctt gaccagggct ttaactgcag agtcacatgt tgacactgac
    14221 ttaacaaagc cttacattaa gtgggatttg ttaaaatatg acttcacgga agagaggtta
    14281 aaactctttg accgttattt taaatattgg gatcagacat accacccaaa ttgtgttaac
    14341 tgtttggatg acagatgcat tctgcattgt gcaaacttta atgttttatt ctctacagtg
    14401 ttcccaccta caagttttgg accactagtg agaaaaatat ttgttgatgg tgttccattt
    14461 gtagtttcaa ctggatacca cttcagagag ctaggtgttg tacataatca ggatgtaaac
    14521 ttacatagct ctagacttag ttttaaggaa ttacttgtgt atgctgctga ccctgctatg
    14581 cacgctgctt ctggtaatct attactagat aaacgcacta cgtgcttttc agtagctgca
    14641 cttactaaca atgttgcttt tcaaactgtc aaacccggta attttaacaa agacttctat
    14701 gactttgctg tgtctaaggg tttctttaag gaaggaagtt ctgttgaatt aaaacacttc
    14761 ttctttgctc aggatggtaa tgctgctatc agcgattatg actactatcg ttataatcta
    14821 ccaacaatgt gtgatatcag acaactacta tttgtagttg aagttgttga taagtacttt
    14881 gattgttacg atggtggctg tattaatgct aaccaagtca tcgtcaacaa cctagacaaa
    14941 tcagctggtt ttccatttaa taaatggggt aaggctagac tttattatga ttcaatgagt
    15001 tatgaggatc aagatgcact tttcgcatat acaaaacgta atgtcatccc tactataact
    15061 caaatgaatc ttaagtatgc cattagtgca aagaatagag ctcgcaccgt agctggtgtc
    15121 tctatctgta gtactatgac caatagacag tttcatcaaa aattattgaa atcaatagcc
    15181 gccactagag gagctactgt agtaattgga acaagcaaat tctatggtgg ttggcacaac
    15241 atgttaaaaa ctgtttatag tgatgtagaa aaccctcacc ttatgggttg ggattatcct
    15301 aaatgtgata gagccatgcc taacatgctt agaattatgg cctcacttgt tcttgctcgc
    15361 aaacatacaa cgtgttgtag cttgtcacac cgtttctata gattagctaa tgagtgtgct
    15421 caagtattga gtgaaatggt catgtgtggc ggttcactat atgttaaacc aggtggaacc
    15481 tcatcaggag atgccacaac tgcttatgct aatagtgttt ttaacatttg tcaagctgtc
    15541 acggccaatg ttaatgcact tttatctact gatggtaaca aaattgccga taagtatgtc
    15601 cgcaatttac aacacagact ttatgagtgt ctctatagaa atagagatgt tgacacagac
    15661 tttgtgaatg agttttacgc atatttgcgt aaacatttct caatgatgat actctctgac
    15721 gatgctgttg tgtgtttcaa tagcacttat gcatctcaag gtctagtggc tagcataaag
    15781 aactttaagt cagttcttta ttatcaaaac aatgttttta tgtctgaagc aaaatgttgg
    15841 actgagactg accttactaa aggacctcat gaattttgct ctcaacatac aatgctagtt
    15901 aaacagggtg atgattatgt gtaccttcct tacccagatc catcaagaat cctaggggcc
    15961 ggctgttttg tagatgatat cgtaaaaaca gatggtacac ttatgattga acggttcgtg
    16021 tctttagcta tagatgctta cccacttact aaacatccta atcaggagta tgctgatgtc
    16081 tttcatttgt acttacaata cataagaaag ctacatgatg agttaacagg acacatgtta
    16141 gacatgtatt ctgttatgct tactaatgat aacacttcaa ggtattggga acctgagttt
    16201 tatgaggcta tgtacacacc gcatacagtc ttacaggctg ttggggcttg tgttctttgc
    16261 aattcacaga cttcattaag atgtggtgct tgcatacgta gaccattctt atgttgtaaa
    16321 tgctgttacg accatgtcat atcaacatca cataaattag tcttgtctgt taatccgtat
    16381 gtttgcaatg ctccaggttg tgatgtcaca gatgtgactc aactttactt aggaggtatg
    16441 agctattatt gtaaatcaca taaaccaccc attagttttc cattgtgtgc taatggacaa
    16501 gtttttggtt tatataaaaa tacatgtgtt ggtagcgata atgttactga ctttaatgca
    16561 attgcaacat gtgactggac aaatgctggt gattacattt tagctaacac ctgtactgaa
    16621 agactcaagc tttttgcagc agaaacgctc aaagctactg aggagacatt taaactgtct
    16681 tatggtattg ctactgtacg tgaagtgctg tctgacagag aattacatct ttcatgggaa
    16741 gttggtaaac ctagaccacc acttaaccga aattatgtct ttactggtta tcgtgtaact
    16801 aaaaacagta aagtacaaat aggagagtac acctttgaaa aaggtgacta tggtgatgct
    16861 gttgtttacc gaggtacaac aacttacaaa ttaaatgttg gtgattattt tgtgctgaca
    16921 tcacatacag taatgccatt aagtgcacct acactagtgc cacaagagca ctatgttaga
    16981 attactggct tatacccaac actcaatatc tcagatgagt tttctagcaa tgttgcaaat
    17041 tatcaaaagg ttggtatgca aaagtattct acactccagg gaccacctgg tactggtaag
    17101 agtcattttg ctattggcct agctctctac tacccttctg ctcgcatagt gtatacagct
    17161 tgctctcatg ccgctgttga tgcactatgt gagaaggcat taaaatattt gcctatagat
    17221 aaatgtagta gaattatacc tgcacgtgct cgtgtagagt gttttgataa attcaaagtg
    17281 aattcaacat tagaacagta tgtcttttgt actgtaaatg cattgcctga gacgacagca
    17341 gatatagttg tctttgatga aatttcaatg gccacaaatt atgatttgag tgttgtcaat
    17401 gccagattac gtgctaagca ctatgtgtac attggcgacc ctgctcaatt acctgcacca
    17461 cgcacattgc taactaaggg cacactagaa ccagaatatt tcaattcagt gtgtagactt
    17521 atgaaaacta taggtccaga catgttcctc ggaacttgtc ggcgttgtcc tgctgaaatt
    17581 gttgacactg tgagtgcttt ggtttatgat aataagctta aagcacataa agacaaatca
    17641 gctcaatgct ttaaaatgtt ttataagggt gttatcacgc atgatgtttc atctgcaatt
    17701 aacaggccac aaataggcgt ggtaagagaa ttccttacac gtaaccctgc ttggagaaaa
    17761 gctgtcttta tttcacctta taattcacag aatgctgtag cctcaaagat tttgggacta
    17821 ccaactcaaa ctgttgattc atcacagggc tcagaatatg actatgtcat attcactcaa
    17881 accactgaaa cagctcactc ttgtaatgta aacagattta atgttgctat taccagagca
    17941 aaagtaggca tactttgcat aatgtctgat agagaccttt atgacaagtt gcaatttaca
    18001 agtcttgaaa ttccacgtag gaatgtggca actttacaag ctgaaaatgt aacaggactc
    18061 tttaaagatt gtagtaaggt aatcactggg ttacatccta cacaggcacc tacacacctc
    18121 agtgttgaca ctaaattcaa aactgaaggt ttatgtgttg acatacctgg catacctaag
    18181 gacatgacct atagaagact catctctatg atgggtttta aaatgaatta tcaagttaat
    18241 ggttacccta acatgtttat cacccgcgaa gaagctataa gacatgtacg tgcatggatt
    18301 ggcttcgatg tcgaggggtg tcatgctact agagaagctg ttggtaccaa tttaccttta
    18361 cagctaggtt tttctacagg tgttaaccta gttgctgtac ctacaggtta tgttgataca
    18421 cctaataata cagatttttc cagagttagt gctaaaccac cgcctggaga tcaatttaaa
    18481 cacctcatac cacttatgta caaaggactt ccttggaatg tagtgcgtat aaagattgta
    18541 caaatgttaa gtgacacact taaaaatctc tctgacagag tcgtatttgt cttatgggca
    18601 catggctttg agttgacatc tatgaagtat tttgtgaaaa taggacctga gcgcacctgt
    18661 tgtctatgtg atagacgtgc cacatgcttt tccactgctt cagacactta tgcctgttgg
    18721 catcattcta ttggatttga ttacgtctat aatccgttta tgattgatgt tcaacaatgg
    18781 ggttttacag gtaacctaca aagcaaccat gatctgtatt gtcaagtcca tggtaatgca
    18841 catgtagcta gttgtgatgc aatcatgact aggtgtctag ctgtccacga gtgctttgtt
    18901 aagcgtgttg actggactat tgaatatcct ataattggtg atgaactgaa gattaatgcg
    18961 gcttgtagaa aggttcaaca catggttgtt aaagctgcat tattagcaga caaattccca
    19021 gttcttcacg acattggtaa ccctaaagct attaagtgtg tacctcaagc tgatgtagaa
    19081 tggaagttct atgatgcaca gccttgtagt gacaaagctt ataaaataga agaattattc
    19141 tattcttatg ccacacattc tgacaaattc acagatggtg tatgcctatt ttggaattgc
    19201 aatgtcgata gatatcctgc taattccatt gtttgtagat ttgacactag agtgctatct
    19261 aaccttaact tgcctggttg tgatggtggc agtttgtatg taaataaaca tgcattccac
    19321 acaccagctt ttgataaaag tgcttttgtt aatttaaaac aattaccatt tttctattac
    19381 tctgacagtc catgtgagtc tcatggaaaa caagtagtgt cagatataga ttatgtacca
    19441 ctaaagtctg ctacgtgtat aacacgttgc aatttaggtg gtgctgtctg tagacatcat
    19501 gctaatgagt acagattgta tctcgatgct tataacatga tgatctcagc tggctttagc
    19561 ttgtgggttt acaaacaatt tgatacttat aacctctgga acacttttac aagacttcag
    19621 agtttagaaa atgtggcttt taatgttgta aataagggac actttgatgg acaacagggt
    19681 gaagtaccag tttctatcat taataacact gtttacacaa aagttgatgg tgttgatgta
    19741 gaattgtttg aaaataaaac aacattacct gttaatgtag catttgagct ttgggctaag
    19801 cgcaacatta aaccagtacc agaggtgaaa atactcaata atttgggtgt ggacattgct
    19861 gctaatactg tgatctggga ctacaaaaga gatgctccag cacatatatc tactattggt
    19921 gtttgttcta tgactgacat agccaagaaa ccaactgaaa cgatttgtgc accactcact
    19981 gtcttttttg atggtagagt tgatggtcaa gtagacttat ttagaaatgc ccgtaatggt
    20041 gttcttatta cagaaggtag tgttaaaggt ttacaaccat ctgtaggtcc caaacaagct
    20101 agtcttaatg gagtcacatt aattggagaa gccgtaaaaa cacagttcaa ttattataag
    20161 aaagttgatg gtgttgtcca acaattacct gaaacttact ttactcagag tagaaattta
    20221 caagaattta aacccaggag tcaaatggaa attgatttct tagaattagc tatggatgaa
    20281 ttcattgaac ggtataaatt agaaggctat gccttcgaac atatcgttta tggagatttt
    20341 agtcatagtc agttaggtgg tttacatcta ctgattggac tagctaaacg ttttaaggaa
    20401 tcaccttttg aattagaaga ttttattcct atggacagta cagttaaaaa ctatttcata
    20461 acagatgcgc aaacaggttc atctaagtgt gtgtgttctg ttattgattt attacttgat
    20521 gattttgttg aaataataaa atcccaagat ttatctgtag tttctaaggt tgtcaaagtg
    20581 actattgact atacagaaat ttcatttatg ctttggtgta aagatggcca tgtagaaaca
    20641 ttttacccaa aattacaatc tagtcaagcg tggcaaccgg gtgttgctat gcctaatctt
    20701 tacaaaatgc aaagaatgct attagaaaag tgtgaccttc aaaattatgg tgatagtgca
    20761 acattaccta aaggcataat gatgaatgtc gcaaaatata ctcaactgtg tcaatattta
    20821 aacacattaa cattagctgt accctataat atgagagtta tacattttgg tgctggttct
    20881 gataaaggag ttgcaccagg tacagctgtt ttaagacagt ggttgcctac gggtacgctg
    20941 cttgtcgatt cagatcttaa tgactttgtc tctgatgcag attcaacttt gattggtgat
    21001 tgtgcaactg tacatacagc taataaatgg gatctcatta ttagtgatat gtacgaccct
    21061 aagactaaaa atgttacaaa agaaaatgac tctaaagagg gttttttcac ttacatttgt
    21121 gggtttatac aacaaaagct agctcttgga ggttccgtgg ctataaagat aacagaacat
    21181 tcttggaatg ctgatcttta taagctcatg ggacacttcg catggtggac agcctttgtt
    21241 actaatgtga atgcgtcatc atctgaagca tttttaattg gatgtaatta tcttggcaaa
    21301 ccacgcgaac aaatagatgg ttatgtcatg catgcaaatt acatattttg gaggaataca
    21361 aatccaattc agttgtcttc ctattcttta tttgacatga gtaaatttcc ccttaaatta
    21421 aggggtactg ctgttatgtc tttaaaagaa ggtcaaatca atgatatgat tttatctctt
    21481 cttagtaaag gtagacttat aattagagaa aacaacagag ttgttatttc tagtgatgtt
    21541 cttgttaaca actaaacgaa caatgtttgt ttttcttgtt ttattgccac tagtctctag
    21601 tcagtgtgtt aatcttacaa ccagaactca attaccccct gcatacacta attctttcac
    21661 acgtggtgtt tattaccctg acaaagtttt cagatcctca gttttacatt caactcagga
    21721 cttgttctta cctttctttt ccaatgttac ttggttccat gctatacatg tctctgggac
    21781 caatggtact aagaggtttg ataaccctgt cctaccattt aatgatggtg tttattttgc
    21841 ttccactgag aagtctaaca taataagagg ctggattttt ggtactactt tagattcgaa
    21901 gacccagtcc ctacttattg ttaataacgc tactaatgtt gttattaaag tctgtgaatt
    21961 tcaattttgt aatgatccat ttttgggtgt ttattaccac aaaaacaaca aaagttggat
    22021 ggaaagtgag ttcagagttt attctagtgc gaataattgc acttttgaat atgtctctca
    22081 gccttttctt atggaccttg aaggaaaaca gggtaatttc aaaaatctta gggaatttgt
    22141 gtttaagaat attgatggtt attttaaaat atattctaag cacacgccta ttaatttagt
    22201 gcgtgatctc cctcagggtt tttcggcttt agaaccattg gtagatttgc caataggtat
    22261 taacatcact aggtttcaaa ctttacttgc tttacataga agttatttga ctcctggtga
    22321 ttcttcttca ggttggacag ctggtgctgc agcttattat gtgggttatc ttcaacctag
    22381 gacttttcta ttaaaatata atgaaaatgg aaccattaca gatgctgtag actgtgcact
    22441 tgaccctctc tcagaaacaa agtgtacgtt gaaatccttc actgtagaaa aaggaatcta
    22501 tcaaacttct aactttagag tccaaccaac agaatctatt gttagatttc ctaatattac
    22561 aaacttgtgc ccttttggtg aagtttttaa cgccaccaga tttgcatctg tttatgcttg
    22621 gaacaggaag agaatcagca actgtgttgc tgattattct gtcctatata attccgcatc
    22681 attttccact tttaagtgtt atggagtgtc tcctactaaa ttaaatgatc tctgctttac
    22741 taatgtctat gcagattcat ttgtaattag aggtgatgaa gtcagacaaa tcgctccagg
    22801 gcaaactgga aagattgctg attataatta taaattacca gatgatttta caggctgcgt
    22861 tatagcttgg aattctaaca atcttgattc taaggttggt ggtaattata attacctgta
    22921 tagattgttt aggaagtcta atctcaaacc ttttgagaga gatatttcaa ctgaaatcta
    22981 tcaggccggt agcacacctt gtaatggtgt tgaaggtttt aattgttact ttcctttaca
    23041 atcatatggt ttccaaccca ctaatggtgt tggttaccaa ccatacagag tagtagtact
    23101 ttcttttgaa cttctacatg caccagcaac tgtttgtgga cctaaaaagt ctactaattt
    23161 ggttaaaaac aaatgtgtca atttcaactt caatggttta acaggcacag gtgttcttac
    23221 tgagtctaac aaaaagtttc tgcctttcca acaatttggc agagacattg ctgacactac
    23281 tgatgctgtc cgtgatccac agacacttga gattcttgac attacaccat gttcttttgg
    23341 tggtgtcagt gttataacac caggaacaaa tacttctaac caggttgctg ttctttatca
    23401 ggatgttaac tgcacagaag tccctgttgc tattcatgca gatcaactta ctcctacttg
    23461 gcgtgtttat tctacaggtt ctaatgtttt tcaaacacgt gcaggctgtt taataggggc
    23521 tgaacatgtc aacaactcat atgagtgtga catacccatt ggtgcaggta tatgcgctag
    23581 ttatcagact cagactaatt ctcctcggcg ggcacgtagt gtagctagtc aatccatcat
    23641 tgcctacact atgtcacttg gtgcagaaaa ttcagttgct tactctaata actctattgc
    23701 catacccaca aattttacta ttagtgttac cacagaaatt ctaccagtgt ctatgaccaa
    23761 gacatcagta gattgtacaa tgtacatttg tggtgattca actgaatgca gcaatctttt
    23821 gttgcaatat ggcagttttt gtacacaatt aaaccgtgct ttaactggaa tagctgttga
    23881 acaagacaaa aacacccaag aagtttttgc acaagtcaaa caaatttaca aaacaccacc
    23941 aattaaagat tttggtggtt ttaatttttc acaaatatta ccagatccat caaaaccaag
    24001 caagaggtca tttattgaag atctactttt caacaaagtg acacttgcag atgctggctt
    24061 catcaaacaa tatggtgatt gccttggtga tattgctgct agagacctca tttgtgcaca
    24121 aaagtttaac ggccttactg ttttgccacc tttgctcaca gatgaaatga ttgctcaata
    24181 cacttctgca ctgttagcgg gtacaatcac ttctggttgg acctttggtg caggtgctgc
    24241 attacaaata ccatttgcta tgcaaatggc ttataggttt aatggtattg gagttacaca
    24301 gaatgttctc tatgagaacc aaaaattgat tgccaaccaa tttaatagtg ctattggcaa
    24361 aattcaagac tcactttctt ccacagcaag tgcacttgga aaacttcaag atgtggtcaa
    24421 ccaaaatgca caagctttaa acacgcttgt taaacaactt agctccaatt ttggtgcaat
    24481 ttcaagtgtt ttaaatgata tcctttcacg tcttgacaaa gttgaggctg aagtgcaaat
    24541 tgataggttg atcacaggca gacttcaaag tttgcagaca tatgtgactc aacaattaat
    24601 tagagctgca gaaatcagag cttctgctaa tcttgctgct actaaaatgt cagagtgtgt
    24661 acttggacaa tcaaaaagag ttgatttttg tggaaagggc tatcatctta tgtccttccc
    24721 tcagtcagca cctcatggtg tagtcttctt gcatgtgact tatgtccctg cacaagaaaa
    24781 gaacttcaca actgctcctg ccatttgtca tgatggaaaa gcacactttc ctcgtgaagg
    24841 tgtctttgtt tcaaatggca cacactggtt tgtaacacaa aggaattttt atgaaccaca
    24901 aatcattact acagacaaca catttgtgtc tggtaactgt gatgttgtaa taggaattgt
    24961 caacaacaca gtttatgatc ctttgcaacc tgaattagac tcattcaagg aggagttaga
    25021 taaatatttt aagaatcata catcaccaga tgttgattta ggtgacatct ctggcattaa
    25081 tgcttcagtt gtaaacattc aaaaagaaat tgaccgcctc aatgaggttg ccaagaattt
    25141 aaatgaatct ctcatcgatc tccaagaact tggaaagtat gagcagtata taaaatggcc
    25201 atggtacatt tggctaggtt ttatagctgg cttgattgcc atagtaatgg tgacaattat
    25261 gctttgctgt atgaccagtt gctgtagttg tctcaagggc tgttgttctt gtggatcctg
    25321 ctgcaaattt gatgaagacg actctgagcc agtgctcaaa ggagtcaaat tacattacac
    25381 ataaacgaac ttatggattt gtttatgaga atcttcacaa ttggaactgt aactttgaag
    25441 caaggtgaaa tcaaggatgc tactccttca gattttgttc gcgctactgc aacgataccg
    25501 atacaagcct cactcccttt cggatggctt attgttggcg ttgcacttct tgctgttttt
    25561 cagagcgctt ccaaaatcat aaccctcaaa aagagatggc aactagcact ctccaagggt
    25621 gttcactttg tttgcaactt gctgttgttg tttgtaacag tttactcaca ccttttgctc
    25681 gttgctgctg gccttgaagc cccttttctc tatctttatg ctttagtcta cttcttgcag
    25741 agtataaact ttgtaagaat aataatgagg ctttggcttt gctggaaatg ccgttccaaa
    25801 aacccattac tttatgatgc caactatttt ctttgctggc atactaattg ttacgactat
    25861 tgtatacctt acaatagtgt aacttcttca attgtcatta cttcaggtga tggcacaaca
    25921 agtcctattt ctgaacatga ctaccagatt ggtggttata ctgaaaaatg ggaatctgga
    25981 gtaaaagact gtgttgtatt acacagttac ttcacttcag actattacca gctgtactca
    26041 actcaattga gtacagacac tggtgttgaa catgttacct tcttcatcta caataaaatt
    26101 gttgatgagc ctgaagaaca tgtccaaatt cacacaatcg acggttcatc cggagttgtt
    26161 aatccagtaa tggaaccaat ttatgatgaa ccgacgacga ctactagcgt gcctttgtaa
    26221 gcacaagctg atgagtacga acttatgtac tcattcgttt cggaagagac aggtacgtta
    26281 atagttaata gcgtacttct ttttcttgct ttcgtggtat tcttgctagt tacactagcc
    26341 atccttactg cgcttcgatt gtgtgcgtac tgctgcaata ttgttaacgt gagtcttgta
    26401 aaaccttctt tttacgttta ctctcgtgtt aaaaatctga attcttctag agttcctgat
    26461 cttctggtct aaacgaacta aatattatat tagtttttct gtttggaact ttaattttag
    26521 ccatggcaga ttccaacggt actattaccg ttgaagagct taaaaagctc cttgaacaat
    26581 ggaacctagt aataggtttc ctattcctta catggatttg tcttctacaa tttgcctatg
    26641 ccaacaggaa taggtttttg tatataatta agttaatttt cctctggctg ttatggccag
    26701 taactttagc ttgttttgtg cttgctgctg tttacagaat aaattggatc accggtggaa
    26761 ttgctatcgc aatggcttgt cttgtaggct tgatgtggct cagctacttc attgcttctt
    26821 tcagactgtt tgcgcgtacg cgttccatgt ggtcattcaa tccagaaact aacattcttc
    26881 tcaacgtgcc actccatggc actattctga ccagaccgct tctagaaagt gaactcgtaa
    26941 tcggagctgt gatccttcgt ggacatcttc gtattgctgg acaccatcta ggacgctgtg
    27001 acatcaagga cctgcctaaa gaaatcactg ttgctacatc acgaacgctt tcttattaca
    27061 aattgggagc ttcgcagcgt gtagcaggtg actcaggttt tgctgcatac agtcgctaca
    27121 ggattggcaa ctataaatta aacacagacc attccagtag cagtgacaat attgctttgc
    27181 ttgtacagta agtgacaaca gatgtttcat ctcgttgact ttcaggttac tatagcagag
    27241 atattactaa ttattatgag gacttttaaa gtttccattt ggaatcttga ttacatcata
    27301 aacctcataa ttaaaaattt atctaagtca ctaactgaga ataaatattc tcaattagat
    27361 gaagagcaac caatggagat tgattaaacg aacatgaaaa ttattctttt cttggcactg
    27421 ataacactcg ctacttgtga gctttatcac taccaagagt gtgttagagg tacaacagta
    27481 cttttaaaag aaccttgctc ttctggaaca tacgagggca attcaccatt tcatcctcta
    27541 gctgataaca aatttgcact gacttgcttt agcactcaat ttgcttttgc ttgtcctgac
    27601 ggcgtaaaac acgtctatca gttacgtgcc agatcagttt cacctaaact gttcatcaga
    27661 caagaggaag ttcaagaact ttactctcca atttttctta ttgttgcggc aatagtgttt
    27721 ataacacttt gcttcacact caaaagaaag acagaatgat tgaactttca ttaattgact
    27781 tctatttgtg ctttttagcc tttctgctat tccttgtttt aattatgctt attatctttt
    27841 ggttctcact tgaactgcaa gatcataatg aaacttgtca cgcctaaacg aacatgaaat
    27901 ttcttgtttt cttaggaatc atcacaactg tagctgcatt tcaccaagaa tgtagtttac
    27961 agtcatgtac tcaacatcaa ccatatgtag ttgatgaccc gtgtcctatt cacttctatt
    28021 ctaaatggta tattagagta ggagctagaa aatcagcacc tttaattgaa ttgtgcgtgg
    28081 atgaggctgg ttctaaatca cccattcagt acatcgatat cggtaattat acagtttcct
    28141 gtttaccttt tacaattaat tgccaggaac ctaaattggg tagtcttgta gtgcgttgtt
    28201 cgttctatga agacttttta gagtatcatg acgttcgtgt tgttttagat ttcatctaaa
    28261 cgaacaaact aaaatgtctg ataatggacc ccaaaatcag cgaaatgcac cccgcattac
    28321 gtttggtgga ccctcagatt caactggcag taaccagaat ggagaacgca gtggggcgcg
    28381 atcaaaacaa cgtcggcccc aaggtttacc caataatact gcgtcttggt tcaccgctct
    28441 cactcaacat ggcaaggaag accttaaatt ccctcgagga caaggcgttc caattaacac
    28501 caatagcagt ccagatgacc aaattggcta ctaccgaaga gctaccagac gaattcgtgg
    28561 tggtgacggt aaaatgaaag atctcagtcc aagatggtat ttctactacc taggaactgg
    28621 gccagaagct ggacttccct atggtgctaa caaagacggc atcatatggg ttgcaactga
    28681 gggagccttg aatacaccaa aagatcacat tggcacccgc aatcctgcta acaatgctgc
    28741 aatcgtgcta caacttcctc aaggaacaac attgccaaaa ggcttctacg cagaagggag
    28801 cagaggcggc agtcaagcct cttctcgttc ctcatcacgt agtcgcaaca gttcaagaaa
    28861 ttcaactcca ggcagcagta ggggaacttc tcctgctaga atggctggca atggcggtga
    28921 tgctgctctt gctttgctgc tgcttgacag attgaaccag cttgagagca aaatgtctgg
    28981 taaaggccaa caacaacaag gccaaactgt cactaagaaa tctgctgctg aggcttctaa
    29041 gaagcctcgg caaaaacgta ctgccactaa agcatacaat gtaacacaag ctttcggcag
    29101 acgtggtcca gaacaaaccc aaggaaattt tggggaccag gaactaatca gacaaggaac
    29161 tgattacaaa cattggccgc aaattgcaca atttgccccc agcgcttcag cgttcttcgg
    29221 aatgtcgcgc attggcatgg aagtcacacc ttcgggaacg tggttgacct acacaggtgc
    29281 catcaaattg gatgacaaag atccaaattt caaagatcaa gtcattttgc tgaataagca
    29341 tattgacgca tacaaaacat tcccaccaac agagcctaaa aaggacaaaa agaagaaggc
    29401 tgatgaaact caagccttac cgcagagaca gaagaaacag caaactgtga ctcttcttcc
    29461 tgctgcagat ttggatgatt tctccaaaca attgcaacaa tccatgagca gtgctgactc
    29521 aactcaggcc taaactcatg cagaccacac aaggcagatg ggctatataa acgttttcgc
    29581 ttttccgttt acgatatata gtctactctt gtgcagaatg aattctcgta actacatagc
    29641 acaagtagat gtagttaact ttaatctcac atagcaatct ttaatcagtg tgtaacatta
    29701 gggaggactt gaaagagcca ccacattttc accgaggcca cgcggagtac gatcgagtgt
    29761 acagtgaaca atgctaggga gagctgccta tatggaagag ccctaatgtg taaaattaat
    29821 tttagtagtg ctatccccat gtgattttaa tagcttctta ggagaatgac aaaaaaaaaa
    29881 aaaaaaaaaa aaaaaaaaaa aaa
"""
for s in " \n0123456789":
    cc = cc.replace(s, "")
cc


# In[73]:


cc_v1 = """
1 atattaggtt tttacctacc caggaaaagc caaccaacct cgatctcttg tagatctgtt
       61 ctctaaacga actttaaaat ctgtgtagct gtcgctcggc tgcatgccta gtgcacctac
      121 gcagtataaa caataataaa ttttactgtc gttgacaaga aacgagtaac tcgtccctct
      181 tctgcagact gcttacggtt tcgtccgtgt tgcagtcgat catcagcata cctaggtttc
      241 gtccgggtgt gaccgaaagg taagatggag agccttgttc ttggtgtcaa cgagaaaaca
      301 cacgtccaac tcagtttgcc tgtccttcag gttagagacg tgctagtgcg tggcttcggg
      361 gactctgtgg aagaggccct atcggaggca cgtgaacacc tcaaaaatgg cacttgtggt
      421 ctagtagagc tggaaaaagg cgtactgccc cagcttgaac agccctatgt gttcattaaa
      481 cgttctgatg ccttaagcac caatcacggc cacaaggtcg ttgagctggt tgcagaaatg
      541 gacggcattc agtacggtcg tagcggtata acactgggag tactcgtgcc acatgtgggc
      601 gaaaccccaa ttgcataccg caatgttctt cttcgtaaga acggtaataa gggagccggt
      661 ggtcatagct atggcatcga tctaaagtct tatgacttag gtgacgagct tggcactgat
      721 cccattgaag attatgaaca aaactggaac actaagcatg gcagtggtgc actccgtgaa
      781 ctcactcgtg agctcaatgg aggtgcagtc actcgctatg tcgacaacaa tttctgtggc
      841 ccagatgggt accctcttga ttgcatcaaa gattttctcg cacgcgcggg caagtcaatg
      901 tgcactcttt ccgaacaact tgattacatc gagtcgaaga gaggtgtcta ctgctgccgt
      961 gaccatgagc atgaaattgc ctggttcact gagcgctctg ataagagcta cgagcaccag
     1021 acacccttcg aaattaagag tgccaagaaa tttgacactt tcaaagggga atgcccaaag
     1081 tttgtgtttc ctcttaactc aaaagtcaaa gtcattcaac cacgtgttga aaagaaaaag
     1141 actgagggtt tcatggggcg tatacgctct gtgtaccctg ttgcatctcc acaggagtgt
     1201 aacaatatgc acttgtctac cttgatgaaa tgtaatcatt gcgatgaagt ttcatggcag
     1261 acgtgcgact ttctgaaagc cacttgtgaa cattgtggca ctgaaaattt agttattgaa
     1321 ggacctacta catgtgggta cctacctact aatgctgtag tgaaaatgcc atgtcctgcc
     1381 tgtcaagacc cagagattgg acctgagcat agtgttgcag attatcacaa ccactcaaac
     1441 attgaaactc gactccgcaa gggaggtagg actagatgtt ttggaggctg tgtgtttgcc
     1501 tatgttggct gctataataa gcgtgcctac tgggttcctc gtgctagtgc tgatattggc
     1561 tcaggccata ctggcattac tggtgacaat gtggagacct tgaatgagga tctccttgag
     1621 atactgagtc gtgaacgtgt taacattaac attgttggcg attttcattt gaatgaagag
     1681 gttgccatca ttttggcatc tttctctgct tctacaagtg cctttattga cactataaag
     1741 agtcttgatt acaagtcttt caaaaccatt gttgagtcct gcggtaacta taaagttacc
     1801 aagggaaagc ccgtaaaagg tgcttggaac attggacaac agagatcagt tttaacacca
     1861 ctgtgtggtt ttccctcaca ggctgctggt gttatcagat caatttttgc gcgcacactt
     1921 gatgcagcaa accactcaat tcctgatttg caaagagcag ctgtcaccat acttgatggt
     1981 atttctgaac agtcattacg tcttgtcgac gccatggttt atacttcaga cctgctcacc
     2041 aacagtgtca ttattatggc atatgtaact ggtggtcttg tacaacagac ttctcagtgg
     2101 ttgtctaatc ttttgggcac tactgttgaa aaactcaggc ctatctttga atggattgag
     2161 gcgaaactta gtgcaggagt tgaatttctc aaggatgctt gggagattct caaatttctc
     2221 attacaggtg tttttgacat cgtcaagggt caaatacagg ttgcttcaga taacatcaag
     2281 gattgtgtaa aatgcttcat tgatgttgtt aacaaggcac tcgaaatgtg cattgatcaa
     2341 gtcactatcg ctggcgcaaa gttgcgatca ctcaacttag gtgaagtctt catcgctcaa
     2401 agcaagggac tttaccgtca gtgtatacgt ggcaaggagc agctgcaact actcatgcct
     2461 cttaaggcac caaaagaagt aacctttctt gaaggtgatt cacatgacac agtacttacc
     2521 tctgaggagg ttgttctcaa gaacggtgaa ctcgaagcac tcgagacgcc cgttgatagc
     2581 ttcacaaatg gagctatcgt tggcacacca gtctgtgtaa atggcctcat gctcttagag
     2641 attaaggaca aagaacaata ctgcgcattg tctcctggtt tactggctac aaacaatgtc
     2701 tttcgcttaa aagggggtgc accaattaaa ggtgtaacct ttggagaaga tactgtttgg
     2761 gaagttcaag gttacaagaa tgtgagaatc acatttgagc ttgatgaacg tgttgacaaa
     2821 gtgcttaatg aaaagtgctc tgtctacact gttgaatccg gtaccgaagt tactgagttt
     2881 gcatgtgttg tagcagaggc tgttgtgaag actttacaac cagtttctga tctccttacc
     2941 aacatgggta ttgatcttga tgagtggagt gtagctacat tctacttatt tgatgatgct
     3001 ggtgaagaaa acttttcatc acgtatgtat tgttcctttt accctccaga tgaggaagaa
     3061 gaggacgatg cagagtgtga ggaagaagaa attgatgaaa cctgtgaaca tgagtacggt
     3121 acagaggatg attatcaagg tctccctctg gaatttggtg cctcagctga aacagttcga
     3181 gttgaggaag aagaagagga agactggctg gatgatacta ctgagcaatc agagattgag
     3241 ccagaaccag aacctacacc tgaagaacca gttaatcagt ttactggtta tttaaaactt
     3301 actgacaatg ttgccattaa atgtgttgac atcgttaagg aggcacaaag tgctaatcct
     3361 atggtgattg taaatgctgc taacatacac ctgaaacatg gtggtggtgt agcaggtgca
     3421 ctcaacaagg caaccaatgg tgccatgcaa aaggagagtg atgattacat taagctaaat
     3481 ggccctctta cagtaggagg gtcttgtttg ctttctggac ataatcttgc taagaagtgt
     3541 ctgcatgttg ttggacctaa cctaaatgca ggtgaggaca tccagcttct taaggcagca
     3601 tatgaaaatt tcaattcaca ggacatctta cttgcaccat tgttgtcagc aggcatattt
     3661 ggtgctaaac cacttcagtc tttacaagtg tgcgtgcaga cggttcgtac acaggtttat
     3721 attgcagtca atgacaaagc tctttatgag caggttgtca tggattatct tgataacctg
     3781 aagcctagag tggaagcacc taaacaagag gagccaccaa acacagaaga ttccaaaact
     3841 gaggagaaat ctgtcgtaca gaagcctgtc gatgtgaagc caaaaattaa ggcctgcatt
     3901 gatgaggtta ccacaacact ggaagaaact aagtttctta ccaataagtt actcttgttt
     3961 gctgatatca atggtaagct ttaccatgat tctcagaaca tgcttagagg tgaagatatg
     4021 tctttccttg agaaggatgc accttacatg gtaggtgatg ttatcactag tggtgatatc
     4081 acttgtgttg taataccctc caaaaaggct ggtggcacta ctgagatgct ctcaagagct
     4141 ttgaagaaag tgccagttga tgagtatata accacgtacc ctggacaagg atgtgctggt
     4201 tatacacttg aggaagctaa gactgctctt aagaaatgca aatctgcatt ttatgtacta
     4261 ccttcagaag cacctaatgc taaggaagag attctaggaa ctgtatcctg gaatttgaga
     4321 gaaatgcttg ctcatgctga agagacaaga aaattaatgc ctatatgcat ggatgttaga
     4381 gccataatgg caaccatcca acgtaagtat aaaggaatta aaattcaaga gggcatcgtt
     4441 gactatggtg tccgattctt cttttatact agtaaagagc ctgtagcttc tattattacg
     4501 aagctgaact ctctaaatga gccgcttgtc acaatgccaa ttggttatgt gacacatggt
     4561 tttaatcttg aagaggctgc gcgctgtatg cgttctctta aagctcctgc cgtagtgtca
     4621 gtatcatcac cagatgctgt tactacatat aatggatacc tcacttcgtc atcaaagaca
     4681 tctgaggagc actttgtaga aacagtttct ttggctggct cttacagaga ttggtcctat
     4741 tcaggacagc gtacagagtt aggtgttgaa tttcttaagc gtggtgacaa aattgtgtac
     4801 cacactctgg agagccccgt cgagtttcat cttgacggtg aggttctttc acttgacaaa
     4861 ctaaagagtc tcttatccct gcgggaggtt aagactataa aagtgttcac aactgtggac
     4921 aacactaatc tccacacaca gcttgtggat atgtctatga catatggaca gcagtttggt
     4981 ccaacatact tggatggtgc tgatgttaca aaaattaaac ctcatgtaaa tcatgagggt
     5041 aagactttct ttgtactacc tagtgatgac acactacgta gtgaagcttt cgagtactac
     5101 catactcttg atgagagttt tcttggtagg tacatgtctg ctttaaacca cacaaagaaa
     5161 tggaaatttc ctcaagttgg tggtttaact tcaattaaat gggctgataa caattgttat
     5221 ttgtctagtg ttttattagc acttcaacag cttgaagtca aattcaatgc accagcactt
     5281 caagaggctt attatagagc ccgtgctggt gatgctgcta acttttgtgc actcatactc
     5341 gcttacagta ataaaactgt tggcgagctt ggtgatgtca gagaaactat gacccatctt
     5401 ctacagcatg ctaatttgga atctgcaaag cgagttctta atgtggtgtg taaacattgt
     5461 ggtcagaaaa ctactacctt aacgggtgta gaagctgtga tgtatatggg tactctatct
     5521 tatgataatc ttaagacagg tgtttccatt ccatgtgtgt gtggtcgtga tgctacacaa
     5581 tatctagtac aacaagagtc ttcttttgtt atgatgtctg caccacctgc tgagtataaa
     5641 ttacagcaag gtacattctt atgtgcgaat gagtacactg gtaactatca gtgtggtcat
     5701 tacactcata taactgctaa ggagaccctc tatcgtattg acggagctca ccttacaaag
     5761 atgtcagagt acaaaggacc agtgactgat gttttctaca aggaaacatc ttacactaca
     5821 accatcaagc ctgtgtcgta taaactcgat ggagttactt acacagagat tgaaccaaaa
     5881 ttggatgggt attataaaaa ggataatgct tactatacag agcagcctat agaccttgta
     5941 ccaactcaac cattaccaaa tgcgagtttt gataatttca aactcacatg ttctaacaca
     6001 aaatttgctg atgatttaaa tcaaatgaca ggcttcacaa agccagcttc acgagagcta
     6061 tctgtcacat tcttcccaga cttgaatggc gatgtagtgg ctattgacta tagacactat
     6121 tcagcgagtt tcaagaaagg tgctaaatta ctgcataagc caattgtttg gcacattaac
     6181 caggctacaa ccaagacaac gttcaaacca aacacttggt gtttacgttg tctttggagt
     6241 acaaagccag tagatacttc aaattcattt gaagttctgg cagtagaaga cacacaagga
     6301 atggacaatc ttgcttgtga aagtcaacaa cccacctctg aagaagtagt ggaaaatcct
     6361 accatacaga aggaagtcat agagtgtgac gtgaaaacta ccgaagttgt aggcaatgtc
     6421 atacttaaac catcagatga aggtgttaaa gtaacacaag agttaggtca tgaggatctt
     6481 atggctgctt atgtggaaaa cacaagcatt accattaaga aacctaatga gctttcacta
     6541 gccttaggtt taaaaacaat tgccactcat ggtattgctg caattaatag tgttccttgg
     6601 agtaaaattt tggcttatgt caaaccattc ttaggacaag cagcaattac aacatcaaat
     6661 tgcgctaaga gattagcaca acgtgtgttt aacaattata tgccttatgt gtttacatta
     6721 ttgttccaat tgtgtacttt tactaaaagt accaattcta gaattagagc ttcactacct
     6781 acaactattg ctaaaaatag tgttaagagt gttgctaaat tatgtttgga tgccggcatt
     6841 aattatgtga agtcacccaa attttctaaa ttgttcacaa tcgctatgtg gctattgttg
     6901 ttaagtattt gcttaggttc tctaatctgt gtaactgctg cttttggtgt actcttatct
     6961 aattttggtg ctccttctta ttgtaatggc gttagagaat tgtatcttaa ttcgtctaac
     7021 gttactacta tggatttctg tgaaggttct tttccttgca gcatttgttt aagtggatta
     7081 gactcccttg attcttatcc agctcttgaa accattcagg tgacgatttc atcgtacaag
     7141 ctagacttga caattttagg tctggccgct gagtgggttt tggcatatat gttgttcaca
     7201 aaattctttt atttattagg tctttcagct ataatgcagg tgttctttgg ctattttgct
     7261 agtcatttca tcagcaattc ttggctcatg tggtttatca ttagtattgt acaaatggca
     7321 cccgtttctg caatggttag gatgtacatc ttctttgctt ctttctacta catatggaag
     7381 agctatgttc atatcatgga tggttgcacc tcttcgactt gcatgatgtg ctataagcgc
     7441 aatcgtgcca cacgcgttga gtgtacaact attgttaatg gcatgaagag atctttctat
     7501 gtctatgcaa atggaggccg tggcttctgc aagactcaca attggaattg tctcaattgt
     7561 gacacatttt gcactggtag tacattcatt agtgatgaag ttgctcgtga tttgtcactc
     7621 cagtttaaaa gaccaatcaa ccctactgac cagtcatcgt atattgttga tagtgttgct
     7681 gtgaaaaatg gcgcgcttca cctctacttt gacaaggctg gtcaaaagac ctatgagaga
     7741 catccgctct cccattttgt caatttagac aatttgagag ctaacaacac taaaggttca
     7801 ctgcctatta atgtcatagt ttttgatggc aagtccaaat gcgacgagtc tgcttctaag
     7861 tctgcttctg tgtactacag tcagctgatg tgccaaccta ttctgttgct tgaccaagct
     7921 cttgtatcag acgttggaga tagtactgaa gtttccgtta agatgtttga tgcttatgtc
     7981 gacacctttt cagcaacttt tagtgttcct atggaaaaac ttaaggcact tgttgctaca
     8041 gctcacagcg agttagcaaa gggtgtagct ttagatggtg tcctttctac attcgtgtca
     8101 gctgcccgac aaggtgttgt tgataccgat gttgacacaa aggatgttat tgaatgtctc
     8161 aaactttcac atcactctga cttagaagtg acaggtgaca gttgtaacaa tttcatgctc
     8221 acctataata aggttgaaaa catgacgccc agagatcttg gcgcatgtat tgactgtaat
     8281 gcaaggcata tcaatgccca agtagcaaaa agtcacaatg tttcactcat ctggaatgta
     8341 aaagactaca tgtctttatc tgaacagctg cgtaaacaaa ttcgtagtgc tgccaagaag
     8401 aacaacatac cttttagact aacttgtgct acaactagac aggttgtcaa tgtcataact
     8461 actaaaatct cactcaaggg tggtaagatt gttagtactt gttttaaact tatgcttaag
     8521 gccacattat tgtgcgttct tgctgcattg gtttgttata tcgttatgcc agtacataca
     8581 ttgtcaatcc atgatggtta cacaaatgaa atcattggtt acaaagccat tcaggatggt
     8641 gtcactcgtg acatcatttc tactgatgat tgttttgcaa ataaacatgc tggttttgac
     8701 gcatggttta gccagcgtgg tggttcatac aaaaatgaca aaagctgccc tgtagtagct
     8761 gctatcatta caagagagat tggtttcata gtgcctggct taccgggtac tgtgctgaga
     8821 gcaatcaatg gtgacttctt gcattttcta cctcgtgttt ttagtgctgt tggcaacatt
     8881 tgctacacac cttccaaact cattgagtat agtgattttg ctacctctgc ttgcgttctt
     8941 gctgctgagt gtacaatttt taaggatgct atgggcaaac ctgtgccata ttgttatgac
     9001 actaatttgc tagagggttc tatttcttat agtgagcttc gtccagacac tcgttatgtg
     9061 cttatggatg gttccatcat acagtttcct aacacttacc tggagggttc tgttagagta
     9121 gtaacaactt ttgatgctga gtactgtaga catggtacat gcgaaaggtc agaagtaggt
     9181 atttgcctat ctaccagtgg tagatgggtt cttaataatg agcattacag agctctatca
     9241 ggagttttct gtggtgttga tgcgatgaat ctcatagcta acatctttac tcctcttgtg
     9301 caacctgtgg gtgctttaga tgtgtctgct tcagtagtgg ctggtggtat tattgccata
     9361 ttggtgactt gtgctgccta ctactttatg aaattcagac gtgtttttgg tgagtacaac
     9421 catgttgttg ctgctaatgc acttttgttt ttgatgtctt tcactatact ctgtctggta
     9481 ccagcttaca gctttctgcc gggagtctac tcagtctttt acttgtactt gacattctat
     9541 ttcaccaatg atgtttcatt cttggctcac cttcaatggt ttgccatgtt ttctcctatt
     9601 gtgccttttt ggataacagc aatctatgta ttctgtattt ctctgaagca ctgccattgg
     9661 ttctttaaca actatcttag gaaaagagtc atgtttaatg gagttacatt tagtaccttc
     9721 gaggaggctg ctttgtgtac ctttttgctc aacaaggaaa tgtacctaaa attgcgtagc
     9781 gagacactgt tgccacttac acagtataac aggtatcttg ctctatataa caagtacaag
     9841 tatttcagtg gagccttaga tactaccagc tatcgtgaag cagcttgctg ccacttagca
     9901 aaggctctaa atgactttag caactcaggt gctgatgttc tctaccaacc accacagaca
     9961 tcaatcactt ctgctgttct gcagagtggt tttaggaaaa tggcattccc gtcaggcaaa
    10021 gttgaagggt gcatggtaca agtaacctgt ggaactacaa ctcttaatgg attgtggttg
    10081 gatgacacag tatactgtcc aagacatgtc atttgcacag cagaagacat gcttaatcct
    10141 aactatgaag atctgctcat tcgcaaatcc aaccatagct ttcttgttca ggctggcaat
    10201 gttcaacttc gtgttattgg ccattctatg caaaattgtc tgcttaggct taaagttgat
    10261 acttctaacc ctaagacacc caagtataaa tttgtccgta tccaacctgg tcaaacattt
    10321 tcagttctag catgctacaa tggttcacca tctggtgttt atcagtgtgc catgagacct
    10381 aatcatacca ttaaaggttc tttccttaat ggatcatgtg gtagtgttgg ttttaacatt
    10441 gattatgatt gcgtgtcttt ctgctatatg catcatatgg agcttccaac aggagtacac
    10501 gctggtactg acttagaagg taaattctat ggtccatttg ttgacagaca aactgcacag
    10561 gctgcaggta cagacacaac cataacatta aatgttttgg catggctgta tgctgctgtt
    10621 atcaatggtg ataggtggtt tcttaataga ttcaccacta ctttgaatga ctttaacctt
    10681 gtggcaatga agtacaacta tgaacctttg acacaagatc atgttgacat attgggacct
    10741 ctttctgctc aaacaggaat tgccgtctta gatatgtgtg ctgctttgaa agagctgctg
    10801 cagaatggta tgaatggtcg tactatcctt ggtagcacta ttttagaaga tgagtttaca
    10861 ccatttgatg ttgttagaca atgctctggt gttaccttcc aaggtaagtt caagaaaatt
    10921 gttaagggca ctcatcattg gatgctttta actttcttga catcactatt gattcttgtt
    10981 caaagtacac agtggtcact gtttttcttt gtttacgaga atgctttctt gccatttact
    11041 cttggtatta tggcaattgc tgcatgtgct atgctgcttg ttaagcataa gcacgcattc
    11101 ttgtgcttgt ttctgttacc ttctcttgca acagttgctt actttaatat ggtctacatg
    11161 cctgctagct gggtgatgcg tatcatgaca tggcttgaat tggctgacac tagcttgtct
    11221 ggttataggc ttaaggattg tgttatgtat gcttcagctt tagttttgct tattctcatg
    11281 acagctcgca ctgtttatga tgatgctgct agacgtgttt ggacactgat gaatgtcatt
    11341 acacttgttt acaaagtcta ctatggtaat gctttagatc aagctatttc catgtgggcc
    11401 ttagttattt ctgtaacctc taactattct ggtgtcgtta cgactatcat gtttttagct
    11461 agagctatag tgtttgtgtg tgttgagtat tacccattgt tatttattac tggcaacacc
    11521 ttacagtgta tcatgcttgt ttattgtttc ttaggctatt gttgctgctg ctactttggc
    11581 cttttctgtt tactcaaccg ttacttcagg cttactcttg gtgtttatga ctacttggtc
    11641 tctacacaag aatttaggta tatgaactcc caggggcttt tgcctcctaa gagtagtatt
    11701 gatgctttca agcttaacat taagttgttg ggtattggag gtaaaccatg tatcaaggtt
    11761 gctactgtac agtctaaaat gtctgacgta aagtgcacat ctgtggtact gctctcggtt
    11821 cttcaacaac ttagagtaga gtcatcttct aaattgtggg cacaatgtgt acaactccac
    11881 aatgatattc ttcttgcaaa agacacaact gaagctttcg agaagatggt ttctcttttg
    11941 tctgttttgc tatccatgca gggtgctgta gacattaata ggttgtgcga ggaaatgctc
    12001 gataaccgtg ctactcttca ggctattgct tcagaattta gttctttacc atcatatgcc
    12061 gcttatgcca ctgcccagga ggcctatgag caggctgtag ctaatggtga ttctgaagtc
    12121 gttctcaaaa agttaaagaa atctttgaat gtggctaaat ctgagtttga ccgtgatgct
    12181 gccatgcaac gcaagttgga aaagatggca gatcaggcta tgacccaaat gtacaaacag
    12241 gcaagatctg aggacaagag ggcaaaagta actagtgcta tgcaaacaat gctcttcact
    12301 atgcttagga agcttgataa tgatgcactt aacaacatta tcaacaatgc gcgtgatggt
    12361 tgtgttccac tcaacatcat accattgact acagcagcca aactcatggt tgttgtccct
    12421 gattatggta cctacaagaa cacttgtgat ggtaacacct ttacatatgc atctgcactc
    12481 tgggaaatcc agcaagttgt tgatgcggat agcaagattg ttcaacttag tgaaattaac
    12541 atggacaatt caccaaattt ggcttggcct cttattgtta cagctctaag agccaactca
    12601 gctgttaaac tacagaataa tgaactgagt ccagtagcac tacgacagat gtcctgtgcg
    12661 gctggtacca cacaaacagc ttgtactgat gacaatgcac ttgcctacta taacaattcg
    12721 aagggaggta ggtttgtgct ggcattacta tcagaccacc aagatctcaa atgggctaga
    12781 ttccctaaga gtgatggtac aggtacaatt tacacagaac tggaaccacc ttgtaggttt
    12841 gttacagaca caccaaaagg gcctaaagtg aaatacttgt acttcatcaa aggcttaaac
    12901 aacctaaata gaggtatggt gctgggcagt ttagctgcta cagtacgtct tcaggctgga
    12961 aatgctacag aagtacctgc caattcaact gtgctttcct tctgtgcttt tgcagtagac
    13021 cctgctaaag catataagga ttacctagca agtggaggac aaccaatcac caactgtgtg
    13081 aagatgttgt gtacacacac tggtacagga caggcaatta ctgtaacacc agaagctaac
    13141 atggaccaag agtcctttgg tggtgcttca tgttgtctgt attgtagatg ccacattgac
    13201 catccaaatc ctaaaggatt ctgtgacttg aaaggtaagt acgtccaaat acctaccact
    13261 tgtgctaatg acccagtggg ttttacactt agaaacacag tctgtaccgt ctgcggaatg
    13321 tggaaaggtt atggctgtag ttgtgaccaa ctccgcgaac ccttgatgca gtctgcggat
    13381 gcatcaacgt ttttaaacgg gtttgcggtg taagtgcagc ccgtcttaca ccgtgcggca
    13441 caggcactag tactgatgtc gtctacaggg cttttgatat ttacaacgaa aaagttgctg
    13501 gttttgcaaa gttcctaaaa actaattgct gtcgcttcca ggagaaggat gaggaaggca
    13561 atttattaga ctcttacttt gtagttaaga ggcatactat gtctaactac caacatgaag
    13621 agactattta taacttggtt aaagattgtc cagcggttgc tgtccatgac tttttcaagt
    13681 ttagagtaga tggtgacatg gtaccacata tatcacgtca gcgtctaact aaatacacaa
    13741 tggctgattt agtctatgct ctacgtcatt ttgatgaggg taattgtgat acattaaaag
    13801 aaatactcgt cacatacaat tgctgtgatg atgattattt caataagaag gattggtatg
    13861 acttcgtaga gaatcctgac atcttacgcg tatatgctaa cttaggtgag cgtgtacgcc
    13921 aatcattatt aaagactgta caattctgcg atgctatgcg tgatgcaggc attgtaggcg
    13981 tactgacatt agataatcag gatcttaatg ggaactggta cgatttcggt gatttcgtac
    14041 aagtagcacc aggctgcgga gttcctattg tggattcata ttactcattg ctgatgccca
    14101 tcctcacttt gactagggca ttggctgctg agtcccatat ggatgctgat ctcgcaaaac
    14161 cacttattaa gtgggatttg ctgaaatatg attttacgga agagagactt tgtctcttcg
    14221 accgttattt taaatattgg gaccagacat accatcccaa ttgtattaac tgtttggatg
    14281 ataggtgtat ccttcattgt gcaaacttta atgtgttatt ttctactgtg tttccaccta
    14341 caagttttgg accactagta agaaaaatat ttgtagatgg tgttcctttt gttgtttcaa
    14401 ctggatacca ttttcgtgag ttaggagtcg tacataatca ggatgtaaac ttacatagct
    14461 cgcgtctcag tttcaaggaa cttttagtgt atgctgctga tccagctatg catgcagctt
    14521 ctggcaattt attgctagat aaacgcacta catgcttttc agtagctgca ctaacaaaca
    14581 atgttgcttt tcaaactgtc aaacccggta attttaataa agacttttat gactttgctg
    14641 tgtctaaagg tttctttaag gaaggaagtt ctgttgaact aaaacacttc ttctttgctc
    14701 aggatggcaa cgctgctatc agtgattatg actattatcg ttataatctg ccaacaatgt
    14761 gtgatatcag acaactccta ttcgtagttg aagttgttga taaatacttt gattgttacg
    14821 atggtggctg tattaatgcc aaccaagtaa tcgttaacaa tctggataaa tcagctggtt
    14881 tcccatttaa taaatggggt aaggctagac tttattatga ctcaatgagt tatgaggatc
    14941 aagatgcact tttcgcgtat actaagcgta atgtcatccc tactataact caaatgaatc
    15001 ttaagtatgc cattagtgca aagaatagag ctcgcaccgt agctggtgtc tctatctgta
    15061 gtactatgac aaatagacag tttcatcaga aattattgaa gtcaatagcc gccactagag
    15121 gagctactgt ggtaattgga acaagcaagt tttacggtgg ctggcataat atgttaaaaa
    15181 ctgtttacag tgatgtagaa actccacacc ttatgggttg ggattatcca aaatgtgaca
    15241 gagccatgcc taacatgctt aggataatgg cctctcttgt tcttgctcgc aaacataaca
    15301 cttgctgtaa cttatcacac cgtttctaca ggttagctaa cgagtgtgcg caagtattaa
    15361 gtgagatggt catgtgtggc ggctcactat atgttaaacc aggtggaaca tcatccggtg
    15421 atgctacaac tgcttatgct aatagtgtct ttaacatttg tcaagctgtt acagccaatg
    15481 taaatgcact tctttcaact gatggtaata agatagctga caagtatgtc cgcaatctac
    15541 aacacaggct ctatgagtgt ctctatagaa atagggatgt tgatcatgaa ttcgtggatg
    15601 agttttacgc ttacctgcgt aaacatttct ccatgatgat tctttctgat gatgccgttg
    15661 tgtgctataa cagtaactat gcggctcaag gtttagtagc tagcattaag aactttaagg
    15721 cagttcttta ttatcaaaat aatgtgttca tgtctgaggc aaaatgttgg actgagactg
    15781 accttactaa aggacctcac gaattttgct cacagcatac aatgctagtt aaacaaggag
    15841 atgattacgt gtacctgcct tacccagatc catcaagaat attaggcgca ggctgttttg
    15901 tcgatgatat tgtcaaaaca gatggtacac ttatgattga aaggttcgtg tcactggcta
    15961 ttgatgctta cccacttaca aaacatccta atcaggagta tgctgatgtc tttcacttgt
    16021 atttacaata cattagaaag ttacatgatg agcttactgg ccacatgttg gacatgtatt
    16081 ccgtaatgct aactaatgat aacacctcac ggtactggga acctgagttt tatgaggcta
    16141 tgtacacacc acatacagtc ttgcaggctg taggtgcttg tgtattgtgc aattcacaga
    16201 cttcacttcg ttgcggtgcc tgtattagga gaccattcct atgttgcaag tgctgctatg
    16261 accatgtcat ttcaacatca cacaaattag tgttgtctgt taatccctat gtttgcaatg
    16321 ccccaggttg tgatgtcact gatgtgacac aactgtatct aggaggtatg agctattatt
    16381 gcaagtcaca taagcctccc attagttttc cattatgtgc taatggtcag gtttttggtt
    16441 tatacaaaaa cacatgtgta ggcagtgaca atgtcactga cttcaatgcg atagcaacat
    16501 gtgattggac taatgctggc gattacatac ttgccaacac ttgtactgag agactcaagc
    16561 ttttcgcagc agaaacgctc aaagccactg aggaaacatt taagctgtca tatggtattg
    16621 ccactgtacg cgaagtactc tctgacagag aattgcatct ttcatgggag gttggaaaac
    16681 ctagaccacc attgaacaga aactatgtct ttactggtta ccgtgtaact aaaaatagta
    16741 aagtacagat tggagagtac acctttgaaa aaggtgacta tggtgatgct gttgtgtaca
    16801 gaggtactac gacatacaag ttgaatgttg gtgattactt tgtgttgaca tctcacactg
    16861 taatgccact tagtgcacct actctagtgc cacaagagca ctatgtgaga attactggct
    16921 tgtacccaac actcaacatc tcagatgagt tttctagcaa tgttgcaaat tatcaaaagg
    16981 tcggcatgca aaagtactct acactccaag gaccacctgg tactggtaag agtcattttg
    17041 ccatcggact tgctctctat tacccatctg ctcgcatagt gtatacggca tgctctcatg
    17101 cagctgttga tgccctatgt gaaaaggcat taaaatattt gcccatagat aaatgtagta
    17161 gaatcatacc tgcgcgtgcg cgcgtagagt gttttgataa attcaaagtg aattcaacac
    17221 tagaacagta tgttttctgc actgtaaatg cattgccaga aacaactgct gacattgtag
    17281 tctttgatga aatctctatg gctactaatt atgacttgag tgttgtcaat gctagacttc
    17341 gtgcaaaaca ctacgtctat attggcgatc ctgctcaatt accagccccc cgcacattgc
    17401 tgactaaagg cacactagaa ccagaatatt ttaattcagt gtgcagactt atgaaaacaa
    17461 taggtccaga catgttcctt ggaacttgtc gccgttgtcc tgctgaaatt gttgacactg
    17521 tgagtgcttt agtttatgac aataagctaa aagcacacaa ggataagtca gctcaatgct
    17581 tcaaaatgtt ctacaaaggt gttattacac atgatgtttc atctgcaatc aacagacctc
    17641 aaataggcgt tgtaagagaa tttcttacac gcaatcctgc ttggagaaaa gctgttttta
    17701 tctcacctta taattcacag aacgctgtag cttcaaaaat cttaggattg cctacgcaga
    17761 ctgttgattc atcacagggt tctgaatatg actatgtcat attcacacaa actactgaaa
    17821 cagcacactc ttgtaatgtc aaccgcttca atgtggctat cacaagggca aaaattggca
    17881 ttttgtgcat aatgtctgat agagatcttt atgacaaact gcaatttaca agtctagaaa
    17941 taccacgtcg caatgtggct acattacaag cagaaaatgt aactggactt tttaaggact
    18001 gtagtaagat cattactggt cttcatccta cacaggcacc tacacacctc agcgttgata
    18061 taaagttcaa gactgaagga ttatgtgttg acataccagg cataccaaag gacatgacct
    18121 accgtagact catctctatg atgggtttca aaatgaatta ccaagtcaat ggttacccta
    18181 atatgtttat cacccgcgaa gaagctattc gtcacgttcg tgcgtggatt ggctttgatg
    18241 tagagggctg tcatgcaact agagatgctg tgggtactaa cctacctctc cagctaggat
    18301 tttctacagg tgttaactta gtagctgtac cgactggtta tgttgacact gaaaataaca
    18361 cagaattcac cagagttaat gcaaaacctc caccaggtga ccagtttaaa catcttatac
    18421 cactcatgta taaaggcttg ccctggaatg tagtgcgtat taagatagta caaatgctca
    18481 gtgatacact gaaaggattg tcagacagag tcgtgttcgt cctttgggcg catggctttg
    18541 agcttacatc aatgaagtac tttgtcaaga ttggacctga aagaacgtgt tgtctgtgtg
    18601 acaaacgtgc aacttgcttt tctacttcat cagatactta tgcctgctgg aatcattctg
    18661 tgggttttga ctatgtctat aacccattta tgattgatgt tcagcagtgg ggctttacgg
    18721 gtaaccttca gagtaaccat gaccaacatt gccaggtaca tggaaatgca catgtggcta
    18781 gttgtgatgc tatcatgact agatgtttag cagtccatga gtgctttgtt aagcgcgttg
    18841 attggtctgt tgaataccct attataggag atgaactgag ggttaattct gcttgcagaa
    18901 aagtacaaca catggttgtg aagtctgcat tgcttgctga taagtttcca gttcttcatg
    18961 acattggaaa tccaaaggct atcaagtgtg tgcctcaggc tgaagtagaa tggaagttct
    19021 acgatgctca gccatgtagt gacaaagctt acaaaataga ggaactcttc tattcttatg
    19081 ctacacatca cgataaattc actgatggtg tttgtttgtt ttggaattgt aacgttgatc
    19141 gttacccagc caatgcaatt gtgtgtaggt ttgacacaag agtcttgtca aacttgaact
    19201 taccaggctg tgatggtggt agtttgtatg tgaataagca tgcattccac actccagctt
    19261 tcgataaaag tgcatttact aatttaaagc aattgccttt cttttactat tctgatagtc
    19321 cttgtgagtc tcatggcaaa caagtagtgt cggatattga ttatgttcca ctcaaatctg
    19381 ctacgtgtat tacacgatgc aatttaggtg gtgctgtttg cagacaccat gcaaatgagt
    19441 accgacagta cttggatgca tataatatga tgatttctgc tggatttagc ctatggattt
    19501 acaaacaatt tgatacttat aacctgtgga atacatttac caggttacag agtttagaaa
    19561 atgtggctta taatgttgtt aataaaggac actttgatgg acacgccggc gaagcacctg
    19621 tttccatcat taataatgct gtttacacaa aggtagatgg tattgatgtg gagatctttg
    19681 aaaataagac aacacttcct gttaatgttg catttgagct ttgggctaag cgtaacatta
    19741 aaccagtgcc agagattaag atactcaata atttgggtgt tgatatcgct gctaatactg
    19801 taatctggga ctacaaaaga gaagccccag cacatgtatc tacaataggt gtctgcacaa
    19861 tgactgacat tgccaagaaa cctactgaga gtgcttgttc ttcacttact gtcttgtttg
    19921 atggtagagt ggaaggacag gtagaccttt ttagaaacgc ccgtaatggt gttttaataa
    19981 cagaaggttc agtcaaaggt ctaacacctt caaagggacc agcacaagct agcgtcaatg
    20041 gagtcacatt aattggagaa tcagtaaaaa cacagtttaa ctactttaag aaagtagacg
    20101 gcattattca acagttgcct gaaacctact ttactcagag cagagactta gaggatttta
    20161 agcccagatc acaaatggaa actgactttc tcgagctcgc tatggatgaa ttcatacagc
    20221 gatataagct cgagggctat gccttcgaac acatcgttta tggagatttc agtcatggac
    20281 aacttggcgg tcttcattta atgataggct tagccaagcg ctcacaagat tcaccactta
    20341 aattagagga ttttatccct atggacagca cagtgaaaaa ttacttcata acagatgcgc
    20401 aaacaggttc atcaaaatgt gtgtgttctg tgattgatct tttacttgat gactttgtcg
    20461 agataataaa gtcacaagat ttgtcagtga tttcaaaagt ggtcaaggtt acaattgact
    20521 atgctgaaat ttcattcatg ctttggtgta aggatggaca tgttgaaacc ttctacccaa
    20581 aactacaagc aagtcaagcg tggcaaccag gtgttgcgat gcctaacttg tacaagatgc
    20641 aaagaatgct tcttgaaaag tgtgaccttc agaattatgg tgaaaatgct gttataccaa
    20701 aaggaataat gatgaatgtc gcaaagtata ctcaactgtg tcaatactta aatacactta
    20761 ctttagctgt accctacaac atgagagtta ttcactttgg tgctggctct gataaaggag
    20821 ttgcaccagg tacagctgtg ctcagacaat ggttgccaac tggcacacta cttgtcgatt
    20881 cagatcttaa tgacttcgtc tccgacgcag attctacttt aattggagac tgtgcaacag
    20941 tacatacggc taataaatgg gaccttatta ttagcgatat gtatgaccct aggaccaaac
    21001 atgtgacaaa agagaatgac tctaaagaag ggtttttcac ttatctgtgt ggatttataa
    21061 agcaaaaact agccctgggt ggttctatag ctgtaaagat aacagagcat tcttggaatg
    21121 ctgaccttta caagcttatg ggccatttct catggtggac agcttttgtt acaaatgtaa
    21181 atgcatcatc atcggaagca tttttaattg gggctaacta tcttggcaag ccgaaggaac
    21241 aaattgatgg ctataccatg catgctaact acattttctg gaggaacaca aatcctatcc
    21301 agttgtcttc ctattcactc tttgacatga gcaaatttcc tcttaaatta agaggaactg
    21361 ctgtaatgtc tcttaaggag aatcaaatca atgatatgat ttattctctt ctggaaaaag
    21421 gtaggcttat cattagagaa aacaacagag ttgtggtttc aagtgatatt cttgttaaca
    21481 actaaacgaa catgtttatt ttcttattat ttcttactct cactagtggt agtgaccttg
    21541 accggtgcac cacttttgat gatgttcaag ctcctaatta cactcaacat acttcatcta
    21601 tgaggggggt ttactatcct gatgaaattt ttagatcaga cactctttat ttaactcagg
    21661 atttatttct tccattttat tctaatgtta cagggtttca tactattaat catacgtttg
    21721 gcaaccctgt catacctttt aaggatggta tttattttgc tgccacagag aaatcaaatg
    21781 ttgtccgtgg ttgggttttt ggttctacca tgaacaacaa gtcacagtcg gtgattatta
    21841 ttaacaattc tactaatgtt gttatacgag catgtaactt tgaattgtgt gacaaccctt
    21901 tctttgctgt ttctaaaccc atgggtacac agacacatac tatgatattc gataatgcat
    21961 ttaattgcac tttcgagtac atatctgatg ccttttcgct tgatgtttca gaaaagtcag
    22021 gtaattttaa acacttacga gagtttgtgt ttaaaaataa agatgggttt ctctatgttt
    22081 ataagggcta tcaacctata gatgtagttc gtgatctacc ttctggtttt aacactttga
    22141 aacctatttt taagttgcct cttggtatta acattacaaa ttttagagcc attcttacag
    22201 ccttttcacc tgctcaagac atttggggca cgtcagctgc agcctatttt gttggctatt
    22261 taaagccaac tacatttatg ctcaagtatg atgaaaatgg tacaatcaca gatgctgttg
    22321 attgttctca aaatccactt gctgaactca aatgctctgt taagagcttt gagattgaca
    22381 aaggaattta ccagacctct aatttcaggg ttgttccctc aggagatgtt gtgagattcc
    22441 ctaatattac aaacttgtgt ccttttggag aggtttttaa tgctactaaa ttcccttctg
    22501 tctatgcatg ggagagaaaa aaaatttcta attgtgttgc tgattactct gtgctctaca
    22561 actcaacatt tttttcaacc tttaagtgct atggcgtttc tgccactaag ttgaatgatc
    22621 tttgcttctc caatgtctat gcagattctt ttgtagtcaa gggagatgat gtaagacaaa
    22681 tagcgccagg acaaactggt gttattgctg attataatta taaattgcca gatgatttca
    22741 tgggttgtgt ccttgcttgg aatactagga acattgatgc tacttcaact ggtaattata
    22801 attataaata taggtatctt agacatggca agcttaggcc ctttgagaga gacatatcta
    22861 atgtgccttt ctcccctgat ggcaaacctt gcaccccacc tgctcttaat tgttattggc
    22921 cattaaatga ttatggtttt tacaccacta ctggcattgg ctaccaacct tacagagttg
    22981 tagtactttc ttttgaactt ttaaatgcac cggccacggt ttgtggacca aaattatcca
    23041 ctgaccttat taagaaccag tgtgtcaatt ttaattttaa tggactcact ggtactggtg
    23101 tgttaactcc ttcttcaaag agatttcaac catttcaaca atttggccgt gatgtttctg
    23161 atttcactga ttccgttcga gatcctaaaa catctgaaat attagacatt tcaccttgcg
    23221 cttttggggg tgtaagtgta attacacctg gaacaaatgc ttcatctgaa gttgctgttc
    23281 tatatcaaga tgttaactgc actgatgttt ctacagcaat tcatgcagat caactcacac
    23341 cagcttggcg catatattct actggaaaca atgtattcca gactcaagca ggctgtctta
    23401 taggagctga gcatgtcgac acttcttatg agtgcgacat tcctattgga gctggcattt
    23461 gtgctagtta ccatacagtt tctttattac gtagtactag ccaaaaatct attgtggctt
    23521 atactatgtc tttaggtgct gatagttcaa ttgcttactc taataacacc attgctatac
    23581 ctactaactt ttcaattagc attactacag aagtaatgcc tgtttctatg gctaaaacct
    23641 ccgtagattg taatatgtac atctgcggag attctactga atgtgctaat ttgcttctcc
    23701 aatatggtag cttttgcaca caactaaatc gtgcactctc aggtattgct gctgaacagg
    23761 atcgcaacac acgtgaagtg ttcgctcaag tcaaacaaat gtacaaaacc ccaactttga
    23821 aatattttgg tggttttaat ttttcacaaa tattacctga ccctctaaag ccaactaaga
    23881 ggtcttttat tgaggacttg ctctttaata aggtgacact cgctgatgct ggcttcatga
    23941 agcaatatgg cgaatgccta ggtgatatta atgctagaga tctcatttgt gcgcagaagt
    24001 tcaatggact tacagtgttg ccacctctgc tcactgatga tatgattgct gcctacactg
    24061 ctgctctagt tagtggtact gccactgctg gatggacatt tggtgctggc gctgctcttc
    24121 aaataccttt tgctatgcaa atggcatata ggttcaatgg cattggagtt acccaaaatg
    24181 ttctctatga gaaccaaaaa caaatcgcca accaatttaa caaggcgatt agtcaaattc
    24241 aagaatcact tacaacaaca tcaactgcat tgggcaagct gcaagacgtt gttaaccaga
    24301 atgctcaagc attaaacaca cttgttaaac aacttagctc taattttggt gcaatttcaa
    24361 gtgtgctaaa tgatatcctt tcgcgacttg ataaagtcga ggcggaggta caaattgaca
    24421 ggttaattac aggcagactt caaagccttc aaacctatgt aacacaacaa ctaatcaggg
    24481 ctgctgaaat cagggcttct gctaatcttg ctgctactaa aatgtctgag tgtgttcttg
    24541 gacaatcaaa aagagttgac ttttgtggaa agggctacca ccttatgtcc ttcccacaag
    24601 cagccccgca tggtgttgtc ttcctacatg tcacgtatgt gccatcccag gagaggaact
    24661 tcaccacagc gccagcaatt tgtcatgaag gcaaagcata cttccctcgt gaaggtgttt
    24721 ttgtgtttaa tggcacttct tggtttatta cacagaggaa cttcttttct ccacaaataa
    24781 ttactacaga caatacattt gtctcaggaa attgtgatgt cgttattggc atcattaaca
    24841 acacagttta tgatcctctg caacctgagc ttgactcatt caaagaagag ctggacaagt
    24901 acttcaaaaa tcatacatca ccagatgttg atcttggcga catttcaggc attaacgctt
    24961 ctgtcgtcaa cattcaaaaa gaaattgacc gcctcaatga ggtcgctaaa aatttaaatg
    25021 aatcactcat tgaccttcaa gaattgggaa aatatgagca atatattaaa tggccttggt
    25081 atgtttggct cggcttcatt gctggactaa ttgccatcgt catggttaca atcttgcttt
    25141 gttgcatgac tagttgttgc agttgcctca agggtgcatg ctcttgtggt tcttgctgca
    25201 agtttgatga ggatgactct gagccagttc tcaagggtgt caaattacat tacacataaa
    25261 cgaacttatg gatttgttta tgagattttt tactcttaga tcaattactg cacagccagt
    25321 aaaaattgac aatgcttctc ctgcaagtac tgttcatgct acagcaacga taccgctaca
    25381 agcctcactc cctttcggat ggcttgttat tggcgttgca tttcttgctg tttttcagag
    25441 cgctaccaaa ataattgcgc tcaataaaag atggcagcta gccctttata agggcttcca
    25501 gttcatttgc aatttactgc tgctatttgt taccatctat tcacatcttt tgcttgtcgc
    25561 tgcaggtatg gaggcgcaat ttttgtacct ctatgccttg atatattttc tacaatgcat
    25621 caacgcatgt agaattatta tgagatgttg gctttgttgg aagtgcaaat ccaagaaccc
    25681 attactttat gatgccaact actttgtttg ctggcacaca cataactatg actactgtat
    25741 accatataac agtgtcacag atacaattgt cgttactgaa ggtgacggca tttcaacacc
    25801 aaaactcaaa gaagactacc aaattggtgg ttattctgag gataggcact caggtgttaa
    25861 agactatgtc gttgtacatg gctatttcac cgaagtttac taccagcttg agtctacaca
    25921 aattactaca gacactggta ttgaaaatgc tacattcttc atctttaaca agcttgttaa
    25981 agacccaccg aatgtgcaaa tacacacaat cgacggctct tcaggagttg ctaatccagc
    26041 aatggatcca atttatgatg agccgacgac gactactagc gtgcctttgt aagcacaaga
    26101 aagtgagtac gaacttatgt actcattcgt ttcggaagaa acaggtacgt taatagttaa
    26161 tagcgtactt ctttttcttg ctttcgtggt attcttgcta gtcacactag ccatccttac
    26221 tgcgcttcga ttgtgtgcgt actgctgcaa tattgttaac gtgagtttag taaaaccaac
    26281 ggtttacgtc tactcgcgtg ttaaaaatct gaactcttct gaaggagttc ctgatcttct
    26341 ggtctaaacg aactaactat tattattatt ctgtttggaa ctttaacatt gcttatcatg
    26401 gcagacaacg gtactattac cgttgaggag cttaaacaac tcctggaaca atggaaccta
    26461 gtaataggtt tcctattcct agcctggatt atgttactac aatttgccta ttctaatcgg
    26521 aacaggtttt tgtacataat aaagcttgtt ttcctctggc tcttgtggcc agtaacactt
    26581 gcttgttttg tgcttgctgc tgtctacaga attaattggg tgactggcgg gattgcgatt
    26641 gcaatggctt gtattgtagg cttgatgtgg cttagctact tcgttgcttc cttcaggctg
    26701 tttgctcgta cccgctcaat gtggtcattc aacccagaaa caaacattct tctcaatgtg
    26761 cctctccggg ggacaattgt gaccagaccg ctcatggaaa gtgaacttgt cattggtgct
    26821 gtgatcattc gtggtcactt gcgaatggcc ggacactccc tagggcgctg tgacattaag
    26881 gacctgccaa aagagatcac tgtggctaca tcacgaacgc tttcttatta caaattagga
    26941 gcgtcgcagc gtgtaggcac tgattcaggt tttgctgcat acaaccgcta ccgtattgga
    27001 aactataaat taaatacaga ccacgccggt agcaacgaca atattgcttt gctagtacag
    27061 taagtgacaa cagatgtttc atcttgttga cttccaggtt acaatagcag agatattgat
    27121 tatcattatg aggactttca ggattgctat ttggaatctt gacgttataa taagttcaat
    27181 agtgagacaa ttatttaagc ctctaactaa gaagaattat tcggagttag atgatgaaga
    27241 acctatggag ttagattatc cataaaacga acatgaaaat tattctcttc ctgacattga
    27301 ttgtatttac atcttgcgag ctatatcact atcaggagtg tgttagaggt acgactgtac
    27361 tactaaaaga accttgccca tcaggaacat acgagggcaa ttcaccattt caccctcttg
    27421 ctgacaataa atttgcacta acttgcacta gcacacactt tgcttttgct tgtgctgacg
    27481 gtactcgaca tacctatcag ctgcgtgcaa gatcagtttc accaaaactt ttcatcagac
    27541 aagaggaggt tcaacaagag ctctactcgc cactttttct cattgttgct gctctagtat
    27601 ttttaatact ttgcttcacc attaagagaa agacagaatg aatgagctca ctttaattga
    27661 cttctatttg tgctttttag cctttctgct attccttgtt ttaataatgc ttattatatt
    27721 ttggttttca ctcgaaatcc aggatctaga agaaccttgt accaaagtct aaacgaacat
    27781 gaaacttctc attgttttga cttgtatttc tctatgcagt tgcatatgca ctgtagtaca
    27841 gcgctgtgca tctaataaac ctcatgtgct tgaagatcct tgtaaggtac aacactaggg
    27901 gtaatactta tagcactgct tggctttgtg ctctaggaaa ggttttacct tttcatagat
    27961 ggcacactat ggttcaaaca tgcacaccta atgttactat caactgtcaa gatccagctg
    28021 gtggtgcgct tatagctagg tgttggtacc ttcatgaagg tcaccaaact gctgcattta
    28081 gagacgtact tgttgtttta aataaacgaa caaattaaaa tgtctgataa tggaccccaa
    28141 tcaaaccaac gtagtgcccc ccgcattaca tttggtggac ccacagattc aactgacaat
    28201 aaccagaatg gaggacgcaa tggggcaagg ccaaaacagc gccgacccca aggtttaccc
    28261 aataatactg cgtcttggtt cacagctctc actcagcatg gcaaggagga acttagattc
    28321 cctcgaggcc agggcgttcc aatcaacacc aatagtggtc cagatgacca aattggctac
    28381 taccgaagag ctacccgacg agttcgtggt ggtgacggca aaatgaaaga gctcagcccc
    28441 agatggtact tctattacct aggaactggc ccagaagctt cacttcccta cggcgctaac
    28501 aaagaaggca tcgtatgggt tgcaactgag ggagccttga atacacccaa agaccacatt
    28561 ggcacccgca atcctaataa caatgctgcc accgtgctac aacttcctca aggaacaaca
    28621 ttgccaaaag gcttctacgc agagggaagc agaggcggca gtcaagcctc ttctcgctcc
    28681 tcatcacgta gtcgcggtaa ttcaagaaat tcaactcctg gcagcagtag gggaaattct
    28741 cctgctcgaa tggctagcgg aggtggtgaa actgccctcg cgctattgct gctagacaga
    28801 ttgaaccagc ttgagagcaa agtttctggt aaaggccaac aacaacaagg ccaaactgtc
    28861 actaagaaat ctgctgctga ggcatctaaa aagcctcgcc aaaaacgtac tgccacaaaa
    28921 cagtacaacg tcactcaagc atttgggaga cgtggtccag aacaaaccca aggaaatttc
    28981 ggggaccaag acctaatcag acaaggaact gattacaaac attggccgca aattgcacaa
    29041 tttgctccaa gtgcctctgc attctttgga atgtcacgca ttggcatgga agtcacacct
    29101 tcgggaacat ggctgactta tcatggagcc attaaattgg atgacaaaga tccacaattc
    29161 aaagacaacg tcatactgct gaacaagcac attgacgcat acaaaacatt cccaccaaca
    29221 gagcctaaaa aggacaaaaa gaaaaagact gatgaagctc agcctttgcc gcagagacaa
    29281 aagaagcagc ccactgtgac tcttcttcct gcggctgaca tggatgattt ctccagacaa
    29341 cttcaaaatt ccatgagtgg agcttctgct gattcaactc aggcataaac actcatgatg
    29401 accacacaag gcagatgggc tatgtaaacg ttttcgcaat tccgtttacg atacatagtc
    29461 tactcttgtg cagaatgaat tctcgtaact aaacagcaca agtaggttta gttaacttta
    29521 atctcacata gcaatcttta atcaatgtgt aacattaggg aggacttgaa agagccacca
    29581 cattttcatc gaggccacgc ggagtacgat cgagggtaca gtgaataatg ctagggagag
    29641 ctgcctatat ggaagagccc taatgtgtaa aattaatttt agtagtgcta tccccatgtg
    29701 attttaatag cttcttagga gaatgacaaa aaaaaaaaaa aaaaaaaaaa a
"""
for s in " \n0123456789":
    cc_v1 = cc_v1.replace(s, "")
cc_v1


# In[74]:


len(cc), len(cc_v1)


# In[77]:


# The difference between Sars_v1 (original strain) and Sars_v2 (covid-19)

import editdistance
editdistance.eval(cc, cc_v1)


# In[ ]:




