
class Region:
    def __init__(self,x,y,w,h,name,adj):#x and y are the top left of the region collision box
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name  = name
        self.units = 1
        self.Pl = 0
        self.adj = adj

    def Click_Region(self,pos):
        x,y = pos
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True

grid = []#From first to last arrays, NA,SA,Eur,Afri,Asia,Aus
#North America
grid.append([])
grid[0].append(Region(220,110,50,50,"ALASKA",["NORTHWEST TERRITORIES","ALBERTA"]))
grid[0].append(Region(270,115,130,45,"NORTHWEST TERRITORIES",["GREENLAND","ALASKA","ALBERTA","ONTARIO"]))
grid[0].append(Region(300,160,70,70,"ALBERTA",["ALASKA","NORTHWEST TERRITORIES","ONTARIO","WESTERN US"]))
grid[0].append(Region(375,200,55,30,"ONTARIO",["QUEBEC","EASTERN US","WESTERN US","ALBERTA","NORTHWEST TERRITORIES"]))
grid[0].append(Region(460,180,50,50,"QUEBEC",["GREENLAND","EASTERN US","ONTARIO"]))
grid[0].append(Region(300,230,70,70,"WESTERN US",["ALBERTA","EASTERN US","ONTARIO","MEXICO"]))
grid[0].append(Region(390,270,60,50,"EASTERN US",["WESTERN US","ONTARIO","QUEBEC","MEXICO"]))
grid[0].append(Region(330,360,60,60,"MEXICO",["WESTERN US","EASTERN US","VENEZUELA"]))

#South America
grid.append([])
grid[1].append(Region(390,410,80,40,"VENEZUELA",["MEXICO","PERU","BRAZIL"]))
grid[1].append(Region(390,500,80,40,"PERU",["VENEZUELA","BRAZIL","ARGENTINA"]))
grid[1].append(Region(480,460,80,70,"BRAZIL",["VENEZUELA","PERU","ARGENTINA","NORTH AFRICA"]))
grid[1].append(Region(420,570,60,80,"ARGENTINA",["PERU","BRAZIL"]))

#Europe
grid.append([])
grid[2].append(Region(520,40,80,90,"GREENLAND",["NORTHWEST TERRITORIES","ONTARIO","QUEBEC","ICELAND"]))
grid[2].append(Region(620,150,50,30,"ICELAND",["GREENLAND","GREAT BRITAIN","SCANDINAVIA"]))
grid[2].append(Region(720,130,60,60,"SCANDINAVIA",["UKRAINE","NORTHERN EUROPE","ICELAND","GREAT BRITAIN"]))
grid[2].append(Region(610,230,50,40,"GREAT BRITAIN",["WESTERN EUROPE","ICELAND","SCANDINAVIA","NORTHERN EUROPE"]))
grid[2].append(Region(700,240,60,50,"NORTHERN EUROPE",["SCANDINAVIA","UKRAINE","EASTERN EUROPE","GREAT BRITAIN","WESTERN EUROPE"]))
grid[2].append(Region(610,340,50,50,"WESTERN EUROPE",["EASTERN EUROPE","NORTHERN EUROPE","GREAT BRITAIN"]))
grid[2].append(Region(690,310,80,40,"EASTERN EUROPE",["NORTHERN EUROPE","UKRAINE","NORTHERN EUROPE","MIDDLE EAST"]))
grid[2].append(Region(780,160,80,130,"UKRAINE",["SCANDINAVIA","NORTHERN EUROPE","EASTERN EUROPE","MIDDLE EAST","AFGHANISTAN","URAL"]))

#Africa
grid.append([])
grid[3].append(Region(640,410,70,120,"NORTH AFRICA",["BRAZIL","EGYPT","EAST AFRICA","CONGO"]))
grid[3].append(Region(720,410,100,50,"EGYPT",["EASTERN EUROPE","EAST AFRICA","MIDDLE EAST","NORTH AFRICA"]))
grid[3].append(Region(750,530,50,70,"CONGO",["EAST AFRICA","SOUTH AFRICA"]))
grid[3].append(Region(780,470,60,60,"EAST AFRICA",["CONGO","MADAGASCAR","SOUTHA AFRICA","MIDDLE EAST"]))
grid[3].append(Region(740,610,70,80,"SOUTH AFRICA",["CONGO","EAST AFRICA","MADAGASCAR"]))
grid[3].append(Region(860,630,50,50,"MADAGASCAR",["EAST AFRICA","SOUTH AFRICA"]))

#Asia
grid.append([])
grid[4].append(Region(910,140,40,110,"URAL",["UKRAINE","AFGHANISTAN","CHINA","SIBERIA"]))
grid[4].append(Region(950,100,80,90,"SIBERIA",["URAL","YAKUTSK","IRKUTSK","MONGOLIA","CHINA"]))
grid[4].append(Region(880,270,80,60,"AFGHANISTAN",["UKRAINE","URAL","CHINA","INDIA","MIDDLE EAST"]))
grid[4].append(Region(820,380,70,80,"MIDDLE EAST",["EGYPT","EAST AFRICA","EASTERN EUROPE","UKRAINE","AFGHANISTAN","INDIA"]))
grid[4].append(Region(940,380,70,60,"INDIA",["MIDDLE EAST","AFGHANISTAN","CHINA","SIAM"]))
grid[4].append(Region(1000,310,100,70,"CHINA",["INDIA","SIAM","AFGHANISTAN","MONGOLIA","URAL","SIBERIA"]))
grid[4].append(Region(1040,410,60,50,"SIAM",["INDIA","INDONESIA","CHINA"]))
grid[4].append(Region(1050,100,60,50,"YAKUTSK",["SIBERIA","IRKUTSK","KAMCHATKA"]))
grid[4].append(Region(1050,160,50,80,"IRKUTSK",["SIBERIA","YAKUTSK","KAMCHATKA","MONGOLIA"]))
grid[4].append(Region(1040,250,80,50,"MONGOLIA",["JAPAN","CHINA","SIBERIA","IRKUTSK","KAMCHATKA"]))
grid[4].append(Region(1140,100,60,50,"KAMCHATKA",["MONGOLIA","IRKUTSK","YAKUTSK","ALASKA"]))
grid[4].append(Region(1180,260,30,40,"JAPAN",["MONGOLIA","KAMCHATKA","NEW GUINEA"]))

#Australia
grid.append([])
grid[5].append(Region(1060,520,80,50,"INDONESIA",["SIAM","NEW GUINEA","WESTERN AUSTRALIA"]))
grid[5].append(Region(1160,500,70,40,"NEW GUINEA",["EASTERN AUSTRALIA","INDONESIA","JAPAN","WESTERN AUSTRALIA"]))
grid[5].append(Region(1110,610,60,70,"WESTERN AUSTRALIA",["EASTERN AUSTRALIA","NEW GUINEA","INDONESIA"]))
grid[5].append(Region(1210,590,50,120,"EASTERN AUSTRALIA",["WESTERN AUSTRALIA","NEW GUINEA"]))


def Find_Grid():
    return grid

def Find_Grid_Test():
    a = 1
    for row in grid:
        a += 1
        for reg in row:
            reg.Pl = a//2
            reg.units = 1
    return grid


















