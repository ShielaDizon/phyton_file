#SHIELA DIZON
#PALINDROME CHECKER

#define string
# I use replace to remove all spaces, since remove can't be used in string
# convert the string into list
#reverse the list
#conditional statement

ela = "A man a plan a casa a bait a lag a malt an ami an abr a bayard a liang an apa a jager an adder a gaw a nut an oca a net a caps a rail a karat an amalaka an agron a brev a kit a ballet an eel a bar a lama a dan a patina a grama a tin a manak a japer a pupa an oka a lev a trad a cab an ala a papaya a loma a cam a catalpa a mon a kor a tam a haloid a regal a lub a war a peen a stob a gad a spin a ward a slag a toom a wed a pos a marg a cedar a daraf a wat a dater a carapa a lot a tennis a laic a farer a dame a haemin an agal a tsar a misaim an enate a halo a garrot a gip a rom a lca an elem a yell a ganoin a waver a boma a ball a waxer a tid an agr an app a yaxis a lion a lack a burg a motmot a rata a vil a satrap a mart a rank a lex an annot a pol a tael a drub a nome a dale a batwoman a mara a lob a tarp a res a drawer a rot a doh a nib a saw a harem a gater an imam a llama a let a bel a hamal a gasser a cadi a ramrod dorm a raid a caress a gal a mahaleb a tela a mallam a minaret a gamer a haw a sabin a hod a tor a reward a ser a prat a bola a ram an amowt a bael a daemon a burd a leat a lop a tonn an axel a knar a tram a part a saliva a tar a tomtom a grub a kcal an oil a six a yapp an arg an adit a rex a wallaba a mob a rev a wanion a galley a melena a clamor a pig a torr a gaol a haet an enami a simar a stalag an anime a haem a darer a facial a sinnet a tola a par a caret a dat a waf a radar a decagram a sop a dew a moot a gals a draw an ips a dag a bots a neep a raw a bul a lager a diol a ham a tarok a noma a plat a camaca a mola a yap a paal an abac a dart a vela a kona a pup a rep a jak an amanita a marga a nit a panada a malar a baleen a tell a batik a verb an organa a kalam an atar a kali a rasp a catena a con a tun a wag a redd an areg a jaap an agnail a dray a barb an aim a natl a mag a lati a baas a canal Panama"
ela=ela.replace("","")
ela=ela.lower()
list_ela=list(ela)
reverse_ela=list_ela[::-1]
if reverse_ela==list_ela:
 print ("YES IT'S A PALINDROME")
else:
 print ("NO IT'S NOT A PALINDROME")
