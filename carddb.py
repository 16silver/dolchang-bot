import time

start = time.time()


class card:
    def __init__(self, name, description):
        self.name=name
        self.description=description
        
f = open("dball.txt",'r')        
        
cardlist = []
cardnamelist = []

while True:
    line = str(f.readline())
    if not line:
        break
    tmpname = line.replace("하스스톤 - ","").replace("\n","")
    line1 = str(f.readline())
    while "종류:" not in line1:
        line1 = str(f.readline())
    line2 = str(f.readline())
    job = line2.find("직업제한:")
    jong = line2.find("종족:")
    if "진영" in line2[job+len("직업제한:"):jong]:
        tmpdes = "조직 "
    else:
        tmpdes = line2[job+len("직업제한:"):jong]
    if "-" not in line2[jong+len("종족:"):len(line2)]:
        tmpdes = tmpdes + line2[jong+len("종족:"):len(line2)].replace("\n","")
    rarity = line1.find("등급:")
    cardtype = line1.find("종류:")
    if "-" not in line1[rarity+len("등급:"):len(line1)]:
        tmpdes = tmpdes + line1[rarity+len("등급:"):len(line1)].replace("\n","")
    ccccc = line1[cardtype+len("종류:"):rarity-1]
    tmpdes = tmpdes + ccccc
    
    if ccccc == "영웅":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("생명력:")
            if idx != -1:
                tmpdes = tmpdes + ", 생명력 " + line[idx+len("생명력:"):len(line)-2]
            else:
                idx = line.find("세트:")
                if idx != -1 and "-" not in line[idx+len("세트:"):len(line)-1]:
                    if "고급" in line[idx+len("세트:"):len(line)-1]:
                        tmpdes = "오리지널 " + tmpdes
                    else:
                        tmpdes = line[idx+len("세트:"):len(line)-1] + tmpdes
                else:
                    idx = line.find("영웅 능력")
                    if idx != -1:
                        tmpdes = tmpdes + ", " + line[line.find("<b>"):len(line)].replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                    else:
                        idx = line.find("확장팩:")
                        if idx != -1:
                            tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
                    
            
            
    elif ccccc == "하수인":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("마나비용:")
            if idx != -1:
                tmpdes = tmpdes + ", " + line[idx+len("마나비용:"):len(line)-2] + "코 "
            else:
                idx = line.find("세트:")
                if idx != -1 and "-" not in line[idx+len("세트:"):len(line)-1]:
                    if "고급" in line[idx+len("세트:"):len(line)-1]:
                        tmpdes = "오리지널 " + tmpdes
                    else:
                        tmpdes = line[idx+len("세트:"):len(line)-1] + tmpdes
                else:
                    idx = line.find("공격력:")
                    if idx != -1:
                        idx2 = line.find("생명력:")
                        tmpdes = tmpdes + line[idx+len("공격력:"):idx2-1] + "/" + line[idx2+len("생명력:"):len(line)-2]
                    else:
                        idx = line.find("효과:")
                        if idx != -1:
                            tmpdes = tmpdes + ", " + (line[idx + len("효과:"):len(line)]).replace("<td class=\"align-left\">","").replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                        else:
                            idx = line.find("확장팩:")
                            if idx != -1:
                                tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
    elif ccccc == "영웅 능력":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("마나비용:")
            if idx != -1:
                tmpdes = tmpdes + ", " + line[idx+len("마나비용:"):len(line)-2] + "코스트"
            else:
                idx = line.find("효과:")
                if idx != -1:
                    tmpdes = tmpdes + ", " + (line[idx + len("효과:"):len(line)]).replace("<td class=\"align-left\">","").replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                else:
                    idx = line.find("확장팩:")
                    if idx != -1:
                        tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
    elif ccccc == "주문":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("마나비용:")
            if idx != -1:
                tmpdes = tmpdes + ", " + line[idx+len("마나비용:"):len(line)-2] + "코스트"
            else:
                idx = line.find("효과:")
                if idx != -1:
                    tmpdes = tmpdes + ", " + (line[idx + len("효과:"):len(line)]).replace("<td class=\"align-left\">","").replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                else:
                    idx = line.find("확장팩:")
                    if idx != -1:
                        tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
    elif ccccc == "무기":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("마나비용:")
            if idx != -1:
                tmpdes = tmpdes + ", " + line[idx+len("마나비용:"):len(line)-2] + "코 "
            else:
                idx = line.find("세트:")
                if idx != -1 and "-" not in line[idx+len("세트:"):len(line)-1]:
                    if "고급" in line[idx+len("세트:"):len(line)-1]:
                        tmpdes = "오리지널 " + tmpdes
                    else:
                        tmpdes = line[idx+len("세트:"):len(line)-1] + tmpdes
                else:
                    idx = line.find("공격력:")
                    if idx != -1:
                        idx2 = line.find("내구도:")
                        tmpdes = tmpdes + line[idx+len("공격력:"):idx2-1] + "/" + line[idx2+len("내구도:"):len(line)-2]
                    else:
                        idx = line.find("효과:")
                        if idx != -1:
                            tmpdes = tmpdes + ", " + (line[idx + len("효과:"):len(line)]).replace("<td class=\"align-left\">","").replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                        else:
                            idx = line.find("확장팩:")
                            if idx != -1:
                                tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
    elif ccccc == "영웅 교체":
        line = str(f.readline())
        while (line[0]).isnumeric():
            idx = line.find("마나비용:")
            if idx != -1:
                tmpdes = tmpdes + ", " + line[idx+len("마나비용:"):len(line)-2] + "코스트"
            else:
                idx = line.find("효과:")
                if idx != -1:
                    tmpdes = tmpdes + ", " + (line[idx + len("효과:"):len(line)]).replace("<td class=\"align-left\">","").replace("<b>","").replace("</b>","").replace("<br/>"," ").replace("<i>","").replace("</i>","").strip()
                else:
                    idx = line.find("확장팩:")
                    if idx != -1:
                        tmpdes = line[idx+len("확장팩:"):len(line)-1].replace("<td class=\"align-left\" colspan=\"3\">","").strip() + " " + tmpdes
            line = str(f.readline())
    cardlist.append(card(tmpname,tmpdes))
    cardnamelist.append(tmpname)
    
end = time.time()
