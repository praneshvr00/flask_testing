from flask import Flask, jsonify, request, json

app = Flask(__name__)

# Route to get all items


register_success = {
    "status": "SUCCESS",
    "code": 900,
    "message": "Registered Email successfully"
}
userdata = {
    "email" : "vrpranesh50@gmail.com",
    "password" : "123456"
}
data = {
    "status": "SUCCESS",
    "code": 900,
    "data": [
        {
            "id": 1,
            "name": "fashion",
            "description": "dresses etc.,",
            "image": "fashion.jpg",
            "subcategories": [
                {
                    "id": 1,
                    "name": "pant",
                    "description": "tommy, allen solly, etc.,",
                    "image": None
                },
                {
                    "id": 2,
                    "name": "shirt",
                    "description": "tommy, allen solly, etc.,",
                    "image": None
                }
            ]
        },
        {
            "id": 3,
            "name": "electronics",
            "description": "tv, mobiles, etc.,",
            "image": "electronics.jpg",
            "subcategories": [
                {
                    "id": 3,
                    "name": "tv",
                    "description": "sony, samsung, etc.,",
                    "image": None
                },
                {
                    "id": 4,
                    "name": "mobiles",
                    "description": "sony, samsung, etc.,",
                    "image": None
                }
            ]
        },
        {
            "id": 45,
            "name": "Crystal Zamora",
            "description": "Establish man dream serve simple take sign. Mention and one six think about subject. Mission subject town shoulder different power.",
            "image": "https://placekitten.com/809/29",
            "subcategories": [
                {
                    "id": 5,
                    "name": "Dale Brown",
                    "description": "Movie follow top free. Teacher according room bring thus mean.",
                    "image": None
                },
                {
                    "id": 10,
                    "name": "Cindy Wade",
                    "description": "Statement play reveal run my popular. Debate than leave attack. Majority sit better wind.",
                    "image": None
                },
                {
                    "id": 29,
                    "name": "Paula Huff",
                    "description": "Article cover but join represent few. Per than evening the sure hot. According everybody central director red however. Party agent miss agreement about physical.",
                    "image": None
                },
                {
                    "id": 88,
                    "name": "David Bennett",
                    "description": "Together meet attention early country. Several impact together not result create.\nMillion people husband. Agree until somebody blood. Available seven son rather size next cover thought.",
                    "image": None
                }
            ]
        },
        {
            "id": 33,
            "name": "Michael Bentley",
            "description": "Service push measure strategy production leader rather. Occur land bar father agent chair task.",
            "image": "https://placekitten.com/292/440",
            "subcategories": [
                {
                    "id": 6,
                    "name": "Kimberly Doyle",
                    "description": "Television change explain pressure total fall us. Hear election beyond might school. Probably thus happy. Either her cut night growth down south.",
                    "image": None
                }
            ]
        },
        {
            "id": 20,
            "name": "Jeff Thomas",
            "description": "Every writer position ground others total. Teach fear page knowledge trip believe I. Election no purpose success at.",
            "image": "https://picsum.photos/437/778",
            "subcategories": [
                {
                    "id": 7,
                    "name": "James Lloyd",
                    "description": "A three he majority month.\nRelationship once six as Democrat. Store effect person. Remain involve relationship ten group industry herself defense.",
                    "image": None
                }
            ]
        },
        {
            "id": 4,
            "name": "Brandon Foster",
            "description": "Another west employee score age simple. Expert in property generation guy. News operation government collection. Fire when leave outside environment air.",
            "image": "https://placekitten.com/234/427",
            "subcategories": [
                {
                    "id": 8,
                    "name": "Andrew Bradshaw",
                    "description": "Network fire decade reality future right foot.\nThroughout sing week recently student whose knowledge in. Skill usually down affect plant.",
                    "image": None
                },
                {
                    "id": 32,
                    "name": "Tracey Smith",
                    "description": "Pick four look sense fill stay. Then various draw know may say.\nNice official large level foreign under. Environmental result training red animal news charge.",
                    "image": None
                }
            ]
        },
        {
            "id": 84,
            "name": "Betty Miller",
            "description": "Decade deep respond direction especially carry college mind. Compare head voice understand people voice.\nLikely final easy church doctor consumer firm. Particular specific month doctor.",
            "image": "https://dummyimage.com/787x704",
            "subcategories": [
                {
                    "id": 9,
                    "name": "Mrs. Karen Mullins",
                    "description": "Expert must result machine. Admit wind he these herself arm turn main. Itself Congress section your spend of our.",
                    "image": None
                }
            ]
        },
        {
            "id": 31,
            "name": "Patrick Grimes",
            "description": "Course camera floor item protect. Minute measure hospital media develop middle major.\nParticularly he we yard understand. Institution paper design end.\nArticle business trade such home better.",
            "image": "https://picsum.photos/125/54",
            "subcategories": [
                {
                    "id": 11,
                    "name": "Matthew Edwards",
                    "description": "Degree else form subject music campaign every director. Effort lawyer travel treat style range sense. Growth standard pick listen.",
                    "image": None
                },
                {
                    "id": 77,
                    "name": "Albert Robinson",
                    "description": "Scene administration why carry attention. Turn relate fast four far. Offer finally drive door forward drop. Throw add her anyone interesting executive act.",
                    "image": None
                }
            ]
        },
        {
            "id": 40,
            "name": "Jessica Hernandez",
            "description": "Leader skill PM seek ten. Chance walk despite act describe return. Service onto month project realize relate why. Possible today increase between.",
            "image": "https://picsum.photos/399/931",
            "subcategories": [
                {
                    "id": 12,
                    "name": "Kaitlyn Martinez",
                    "description": "Approach provide show check. Improve it their direction college executive once.\nPerform whole economic long consider receive. American eight game travel south expert.",
                    "image": None
                },
                {
                    "id": 34,
                    "name": "Regina Johnson",
                    "description": "Civil three drug our kitchen away. Seek music work couple not choose television. Then social final top much.",
                    "image": None
                }
            ]
        },
        {
            "id": 23,
            "name": "Elizabeth Thomas",
            "description": "Benefit out total economic.\nExecutive just brother peace yard better. Task hundred such wrong.\nThough scientist today middle. Firm pull likely record none another.",
            "image": "https://placekitten.com/42/1010",
            "subcategories": [
                {
                    "id": 13,
                    "name": "Nancy French",
                    "description": "Financial safe use. Window half outside can. Tend soldier situation part.",
                    "image": None
                }
            ]
        },
        {
            "id": 7,
            "name": "William Page",
            "description": "Hotel oil drive people. Environmental company center fall. Will bank magazine big employee.\nAgency source day local.\nFederal win daughter tough culture moment party.",
            "image": "https://placekitten.com/473/920",
            "subcategories": [
                {
                    "id": 14,
                    "name": "Hannah Ware",
                    "description": "Us get more color heavy power.\nDetail natural safe who. Piece case everything laugh memory everyone. Leave fire tax seven bank call.",
                    "image": None
                }
            ]
        },
        {
            "id": 70,
            "name": "Cory Little",
            "description": "Institution western pattern table letter teach. Wide whom direction food visit.\nStart now son explain personal. Discussion here push spring market.",
            "image": "https://placekitten.com/797/64",
            "subcategories": [
                {
                    "id": 15,
                    "name": "Jessica Carroll",
                    "description": "Meeting break interest course political. They poor parent method main. Add pull lawyer again member form place. Specific take strong break person.",
                    "image": None
                },
                {
                    "id": 62,
                    "name": "Jay Caldwell",
                    "description": "Amount present idea sound leg fund race. Find too main consider indicate skill race. Resource wear window should voice Republican would.\nThen total return. Join population forget.",
                    "image": None
                }
            ]
        },
        {
            "id": 59,
            "name": "Carlos Powell",
            "description": "Huge fast time read red experience. Mission degree nation language reach national speech entire. These president seek activity break wall.",
            "image": "https://dummyimage.com/535x493",
            "subcategories": [
                {
                    "id": 16,
                    "name": "Michael Barber",
                    "description": "Role magazine me cover. Already present president however risk improve million. Last southern nice myself current industry.",
                    "image": None
                }
            ]
        },
        {
            "id": 28,
            "name": "Jonathan Hardy",
            "description": "Ok area tend something dream research onto. Court take drug security treatment direction.\nMorning important simple cell.\nPolice leg sea feel.",
            "image": "https://dummyimage.com/502x576",
            "subcategories": [
                {
                    "id": 17,
                    "name": "Billy Carroll",
                    "description": "Property writer perhaps. Down term keep open training anything seat.\nStrategy huge develop simple. Day officer his will.\nArea serious those. Raise nature behind social.",
                    "image": None
                }
            ]
        },
        {
            "id": 74,
            "name": "Gary Lara",
            "description": "Order window agreement suddenly program. Out responsibility blood town increase whatever customer. Occur new add hear executive.\nDevelop standard world experience statement.",
            "image": "https://picsum.photos/576/263",
            "subcategories": [
                {
                    "id": 18,
                    "name": "Alexis Johnson",
                    "description": "Worry drive any painting soon someone.\nHundred decide series artist everything large face. Number place few hit many pretty yet. Property similar according sell good adult nearly.",
                    "image": None
                },
                {
                    "id": 35,
                    "name": "James Patrick",
                    "description": "Produce stuff space place. Religious rate fall impact structure why. Book drop weight able population.\nYet rock enough team shake eight.",
                    "image": None
                }
            ]
        },
        {
            "id": 86,
            "name": "Gina Stanley",
            "description": "Continue than someone. Notice sport whole share I trial four blue. Among several play large you.\nParty own side. Staff enter account.\nForget run upon eat. Chair suddenly building right eye.",
            "image": "https://placekitten.com/461/730",
            "subcategories": [
                {
                    "id": 19,
                    "name": "Donald Willis",
                    "description": "Mention service center identify provide center. Moment work some chance. Doctor as free ten save history.\nUnder season pay number soldier effort say. Hour back official risk policy camera difference.",
                    "image": None
                },
                {
                    "id": 52,
                    "name": "Michael Lowery",
                    "description": "Particular list rather.\nInto drop win commercial. Give look six miss why.\nMember chance lead suffer environmental practice place. Season mouth serious particular less.",
                    "image": None
                },
                {
                    "id": 65,
                    "name": "Ronald Bowman",
                    "description": "Force high week share. Business yeah head while friend entire fine. Easy about more citizen student style rise. Western sign that mean section hair.",
                    "image": None
                }
            ]
        },
        {
            "id": 87,
            "name": "Cameron Thomas",
            "description": "Myself miss summer development lead. Eight real eye fall.\nMany key thank key around. Recently water own need level opportunity police.\nSong family marriage.\nTheory best mention task century theory.",
            "image": "https://picsum.photos/490/255",
            "subcategories": [
                {
                    "id": 20,
                    "name": "Alexandria Rollins",
                    "description": "Quite economic water our whole him. Size region friend prove old rather really. Change ten suggest today actually.\nThe probably agent tend. Ever phone under and article.",
                    "image": None
                },
                {
                    "id": 30,
                    "name": "Zachary Hopkins",
                    "description": "Week soon send recent heavy treatment. Window time computer wife receive style ability visit.",
                    "image": None
                },
                {
                    "id": 42,
                    "name": "Scott Rocha",
                    "description": "Particularly nice mean machine Mr economic recognize.\nStay example hope ball attack. Animal suggest hair mind. Up moment low.",
                    "image": None
                },
                {
                    "id": 72,
                    "name": "George Wong",
                    "description": "Home board stand dream true back. Teacher or make him study chair. Room media trouble person agree. Film raise agent beautiful name themselves discover.",
                    "image": None
                }
            ]
        },
        {
            "id": 36,
            "name": "Michael Martin",
            "description": "Future many baby energy with. Service woman wish nice sport development upon.\nFinal development family detail site pass. Money happy agree vote benefit treat. Better white arrive whether though.",
            "image": "https://placekitten.com/351/557",
            "subcategories": [
                {
                    "id": 21,
                    "name": "Cory Marshall",
                    "description": "Toward either black through season affect myself. With still perform PM wind.\nSupport player computer program. He still attorney hour never. Step break major bit modern technology back.",
                    "image": None
                }
            ]
        },
        {
            "id": 79,
            "name": "Robert Oneill",
            "description": "Home assume but win speech cause guess agree. Also too else art TV. East green rest approach remember so article.",
            "image": "https://dummyimage.com/786x426",
            "subcategories": [
                {
                    "id": 22,
                    "name": "Alyssa Swanson",
                    "description": "Debate who exist for gas. Over save first white visit house. Whatever her in him car difficult.\nTell type role. Politics place out position question even issue.",
                    "image": None
                },
                {
                    "id": 80,
                    "name": "Anna Mitchell",
                    "description": "Sign allow whose throw west former. Safe story better administration expect true.\nSea team account teacher make difference hour run.",
                    "image": None
                }
            ]
        },
        {
            "id": 43,
            "name": "Jennifer Suarez",
            "description": "This relate out smile sport no about. Eat act generation fast bit billion physical hair. Coach arrive place feeling performance.\nPartner thing military return.\nCost doctor person design.",
            "image": "https://dummyimage.com/225x762",
            "subcategories": [
                {
                    "id": 23,
                    "name": "Brian Pena",
                    "description": "Surface exist fund crime those. Return many travel simply try. Evidence expect beyond study blue.\nAsk case civil reach ever conference.",
                    "image": None
                }
            ]
        },
        {
            "id": 62,
            "name": "Dominic Solomon",
            "description": "Drop increase design seven everything response somebody. Theory walk rich close carry. Billion article how thing hot natural.",
            "image": "https://picsum.photos/640/333",
            "subcategories": [
                {
                    "id": 24,
                    "name": "Thomas Turner",
                    "description": "Less deal PM agreement cover organization. Agree together cover staff.\nFinally bill west. Them civil world range. Where usually customer some your democratic health ask. Political say no house all.",
                    "image": None
                }
            ]
        },
        {
            "id": 77,
            "name": "Anthony Smith",
            "description": "Answer what source my. Quality reveal their. Walk wind out notice take.\nHouse economy pass whom. Enough whether everything guy.\nEdge officer case finish same. Base especially back easy whose method.",
            "image": "https://dummyimage.com/28x748",
            "subcategories": [
                {
                    "id": 25,
                    "name": "Manuel Richardson",
                    "description": "Season join certain American and. Head hair would visit. Bag buy huge.\nInvestment nature play meet. Front budget test person. Its oil whole debate stage surface.",
                    "image": None
                },
                {
                    "id": 102,
                    "name": "Jennifer Howard",
                    "description": "Lot arm bag. Almost task continue skin religious record agreement. Make everything determine.",
                    "image": None
                }
            ]
        },
        {
            "id": 83,
            "name": "Melanie Wilson",
            "description": "This feel movement. Lawyer billion use hot. Wife place mean skill.\nThrow piece free talk those deal despite each. Look painting include.",
            "image": "https://dummyimage.com/241x89",
            "subcategories": [
                {
                    "id": 26,
                    "name": "Ronnie Krueger",
                    "description": "Able view ready likely determine believe strong. Time process well choice.\nAlmost edge benefit. Use vote drop myself. Similar avoid relate you oil sound say.",
                    "image": None
                }
            ]
        },
        {
            "id": 64,
            "name": "Emily Skinner",
            "description": "Prevent appear responsibility growth model. Week great specific.\nTough water water really. National six mouth capital stop center great. Fear money approach friend.",
            "image": "https://picsum.photos/741/733",
            "subcategories": [
                {
                    "id": 27,
                    "name": "Margaret Peters",
                    "description": "Across girl strategy why give stay. Build himself else question east officer society. Start phone various physical direction hotel.",
                    "image": None
                }
            ]
        },
        {
            "id": 50,
            "name": "Jessica Phillips",
            "description": "Else beyond accept thank Republican will especially. Participant show write industry be unit.",
            "image": "https://picsum.photos/952/556",
            "subcategories": [
                {
                    "id": 28,
                    "name": "Sarah Gonzalez",
                    "description": "Class force likely very question these. Again prepare fight now benefit next herself according.\nEnjoy be different. Turn let list before those.",
                    "image": None
                }
            ]
        },
        {
            "id": 5,
            "name": "Henry Washington",
            "description": "Yard anything heart several learn learn certain. Serious century travel full show organization. Ever our Mrs beat set store.",
            "image": "https://picsum.photos/375/339",
            "subcategories": [
                {
                    "id": 31,
                    "name": "Adam Jones",
                    "description": "Hear house artist simply. Summer draw cell rise customer artist. Garden together office fear.\nHappy all cover data. Reality discuss cut sea. Act concern wonder event.",
                    "image": None
                },
                {
                    "id": 71,
                    "name": "Darren Hill",
                    "description": "Black product later science hotel material. Prepare heavy return trouble almost green individual. Several pressure poor.",
                    "image": None
                }
            ]
        },
        {
            "id": 88,
            "name": "Cassandra Thomas",
            "description": "Worker attack mind many Mr drop event pay.\nSort lot student travel. Soldier way stock threat something up that edge. Own item spend region career some international. Close dog as close.",
            "image": "https://picsum.photos/5/276",
            "subcategories": [
                {
                    "id": 33,
                    "name": "Terri Thompson",
                    "description": "Again environment daughter leg. Response week attorney consider design shake provide.",
                    "image": None
                }
            ]
        },
        {
            "id": 17,
            "name": "Elizabeth Boyer",
            "description": "Interview Republican debate decade that ready. Blood kind Mr space idea.\nSame social so hand want. Success everyone maybe use. Mind body head.",
            "image": "https://dummyimage.com/222x957",
            "subcategories": [
                {
                    "id": 36,
                    "name": "James Bridges",
                    "description": "Dinner alone site quality with. Billion ball room street news. Under glass her again.\nTreatment relationship floor little those loss on. Report trial nothing interview foreign alone.",
                    "image": None
                },
                {
                    "id": 67,
                    "name": "Theresa Ewing",
                    "description": "Such up concern option blood ground our. Human dog mind page.\nLast school include treat. Continue create through contain day. Detail fast rich bag.",
                    "image": None
                }
            ]
        },
        {
            "id": 68,
            "name": "Adam Campbell",
            "description": "Build yard special road together everyone why. Guy region night suffer material heavy. But increase which newspaper indeed ask.",
            "image": "https://picsum.photos/994/156",
            "subcategories": [
                {
                    "id": 37,
                    "name": "Jennifer Miller",
                    "description": "Radio little direction these. Goal sound show media.\nKnow glass interview. Rest training site wife control. Pressure forward hand help notice public.",
                    "image": None
                },
                {
                    "id": 60,
                    "name": "Jeffrey Harris",
                    "description": "Position hour present his across half. Husband record yeah country ground later us. That government writer simply officer.",
                    "image": None
                }
            ]
        },
        {
            "id": 11,
            "name": "Gabrielle Williams",
            "description": "Congress PM receive young behind newspaper. Not admit more relate. Happy general cause really nature general citizen.\nChair night western product executive. Fly environment theory home themselves.",
            "image": "https://dummyimage.com/181x217",
            "subcategories": [
                {
                    "id": 38,
                    "name": "Judy Trujillo",
                    "description": "Performance month focus hear. Either hard decision dream summer.\nNotice culture help authority eat gas point simply. Else wrong question likely position front. Style health tax run country.",
                    "image": None
                }
            ]
        },
        {
            "id": 94,
            "name": "Jennifer Johnson",
            "description": "Research position ready.",
            "image": "https://dummyimage.com/719x79",
            "subcategories": [
                {
                    "id": 39,
                    "name": "Jacob Hill",
                    "description": "Car nation exactly be meet.\nExplain national create world though. Call appear former accept positive wide like. Add ago whether behind.",
                    "image": None
                }
            ]
        },
        {
            "id": 18,
            "name": "Kelly Huber",
            "description": "Value when town arrive majority risk. Cup candidate memory its rise day nor.\nDark boy allow. Against human meeting reason senior area later reality. Top himself civil.",
            "image": "https://placekitten.com/596/892",
            "subcategories": [
                {
                    "id": 40,
                    "name": "Nicholas Brown",
                    "description": "Need clearly summer result. Read result practice she pretty religious.",
                    "image": None
                },
                {
                    "id": 89,
                    "name": "Rebecca Stewart",
                    "description": "Court method politics past remain lose. Seat arrive both president out city religious. Get contain measure. Generation hold security peace.",
                    "image": None
                },
                {
                    "id": 96,
                    "name": "Michael Olson",
                    "description": "Detail role most future will.\nCouple responsibility generation pretty. Impact little general glass even. Rise explain western into hot she begin contain.",
                    "image": None
                }
            ]
        },
        {
            "id": 73,
            "name": "Andrew Bennett",
            "description": "Court various minute though big war environmental.\nGroup pick weight. Compare though main father result. Home question baby worry century level Democrat. Owner management traditional ten anyone.",
            "image": "https://dummyimage.com/176x310",
            "subcategories": [
                {
                    "id": 41,
                    "name": "Steven Jenkins",
                    "description": "Over ahead board less heavy institution. Commercial next Congress describe worry. More trip body learn adult group power.\nAsk attention scientist change. Him page do attorney main rate executive.",
                    "image": None
                }
            ]
        },
        {
            "id": 37,
            "name": "Sydney Garcia",
            "description": "Win hope class already. Hour accept today responsibility firm majority animal girl. Seem arm amount technology.",
            "image": "https://placekitten.com/705/112",
            "subcategories": [
                {
                    "id": 43,
                    "name": "Kathleen Knight",
                    "description": "Foot produce white just skill return their. Scene choose particularly research visit save. I threat standard certain us.",
                    "image": None
                },
                {
                    "id": 51,
                    "name": "Tonya Cox",
                    "description": "Nor trouble reveal.\nResponsibility peace paper tax anything. Figure notice themselves machine dark.",
                    "image": None
                }
            ]
        },
        {
            "id": 32,
            "name": "Linda Johnson",
            "description": "Mind guess ground station heart car. Computer organization finish stage model include. Beautiful sea nothing top mouth care. Just morning world drug.",
            "image": "https://picsum.photos/278/96",
            "subcategories": [
                {
                    "id": 44,
                    "name": "Adam Brewer",
                    "description": "Wall grow certain blue care onto. Hour stop cost ago line. Run wish admit kitchen speech.\nYet player language weight song once house south. Bring range method deal financial today.",
                    "image": None
                }
            ]
        },
        {
            "id": 41,
            "name": "Timothy Brown",
            "description": "Job project require check get life. Sort think else magazine family. Summer buy teacher walk imagine also specific.",
            "image": "https://dummyimage.com/312x277",
            "subcategories": [
                {
                    "id": 45,
                    "name": "Kelly Young",
                    "description": "Carry country camera and. Pattern effect responsibility senior option. Population cost new forward.",
                    "image": None
                }
            ]
        },
        {
            "id": 46,
            "name": "Caleb Ayala",
            "description": "Politics somebody popular her production friend. Go course news open. Fly group short year.\nAny walk spring star.",
            "image": "https://dummyimage.com/830x296",
            "subcategories": [
                {
                    "id": 46,
                    "name": "Stephanie Jones",
                    "description": "Available something up. Nor or page star baby such. Note field side.\nTheir per person begin. Front successful house style toward generation. Cut central TV north place.",
                    "image": None
                },
                {
                    "id": 47,
                    "name": "Daniel Barker",
                    "description": "Will shoulder base ground care. Skin very cut cold. Heavy seek whatever election expect.\nKnow require catch. I none different perhaps. Could speak them dog throw.",
                    "image": None
                }
            ]
        },
        {
            "id": 24,
            "name": "Erin Green",
            "description": "Citizen today money business if charge.\nAbility herself half cell measure cause arrive. Language often protect allow. Specific best land cultural.",
            "image": "https://placekitten.com/763/191",
            "subcategories": [
                {
                    "id": 48,
                    "name": "Anthony Greene",
                    "description": "Response pressure leg listen work president step. Usually prevent section. Civil return school fill of activity.",
                    "image": None
                },
                {
                    "id": 57,
                    "name": "Daniel Hardin",
                    "description": "Poor knowledge after officer position it. Seek important local nor. Lead create commercial physical enough computer.",
                    "image": None
                },
                {
                    "id": 104,
                    "name": "Laurie Snyder",
                    "description": "Officer entire everyone poor parent money. Indicate leave behind federal pick determine yes.",
                    "image": None
                }
            ]
        },
        {
            "id": 98,
            "name": "Nathan Charles",
            "description": "Agency artist level international book. She wall imagine reason pressure study.",
            "image": "https://dummyimage.com/819x352",
            "subcategories": [
                {
                    "id": 49,
                    "name": "Jeremy Livingston",
                    "description": "Television before toward morning star real energy. Deep discuss question goal. Example run someone however a customer table about.",
                    "image": None
                }
            ]
        },
        {
            "id": 90,
            "name": "Scott Kennedy",
            "description": "Of watch state million wall. Image measure common star.\nImage ahead voice red standard PM. Lose tax girl among mission.",
            "image": "https://picsum.photos/1012/650",
            "subcategories": [
                {
                    "id": 50,
                    "name": "Dennis Andersen",
                    "description": "Travel effect visit light. Different prove dinner today.\nBehind part somebody design field probably. Trip paper plant maintain. Nice newspaper then view anyone dark on occur.",
                    "image": None
                },
                {
                    "id": 76,
                    "name": "Peggy Thompson",
                    "description": "Value standard Mrs reflect. Business respond their turn teacher program.\nYoung child ball senior. About best sell head moment why.\nLanguage real attack more. Foreign people executive morning.",
                    "image": None
                }
            ]
        },
        {
            "id": 44,
            "name": "Deborah Fritz",
            "description": "Successful spend peace leave someone improve. Pretty provide model half discover. Give because painting authority billion.",
            "image": "https://placekitten.com/498/494",
            "subcategories": [
                {
                    "id": 53,
                    "name": "Patricia Garcia",
                    "description": "East responsibility trip hot. Feel campaign natural line hope between. Just sit ok several.\nDetermine dream majority. Miss dream community true.",
                    "image": None
                }
            ]
        },
        {
            "id": 57,
            "name": "Chad Garrison",
            "description": "Under least finally behavior site Mrs herself put. Fast set act address.",
            "image": "https://dummyimage.com/580x760",
            "subcategories": [
                {
                    "id": 54,
                    "name": "Raymond Casey",
                    "description": "Blood they manager necessary. Industry to statement compare.\nExist wall form into ago her. Least state stop make. Gas for job benefit management alone home.\nAccount own leader product billion.",
                    "image": None
                },
                {
                    "id": 100,
                    "name": "Carolyn Mitchell",
                    "description": "Hit security gun than television food. Yet send yeah cup without the. Various herself apply determine change join.",
                    "image": None
                }
            ]
        },
        {
            "id": 55,
            "name": "Dr. Melanie Hopkins",
            "description": "Throughout social style science green sea. Speak rest focus degree door. Collection move yard machine author.",
            "image": "https://placekitten.com/795/740",
            "subcategories": [
                {
                    "id": 55,
                    "name": "Daisy Wood",
                    "description": "Shoulder story trial. Yard themselves put Congress able suffer.\nBeyond behind room its around so. Area direction exist hit music value. Mind movie senior subject. Hard language entire century.",
                    "image": None
                }
            ]
        },
        {
            "id": 12,
            "name": "Kenneth Sanchez",
            "description": "Technology behavior question new. Important individual camera sort still course.",
            "image": "https://dummyimage.com/211x484",
            "subcategories": [
                {
                    "id": 56,
                    "name": "Aaron Sampson",
                    "description": "Small street finally clearly.\nParent hour seat his turn religious their. Boy my media blood. Fire study look different police son land various. Thus third should north loss reason young.",
                    "image": None
                }
            ]
        },
        {
            "id": 38,
            "name": "Angela Gutierrez",
            "description": "Woman fish agent. Guy piece they surface trouble life manager.\nSomebody but but break word. War often level themselves get matter economic. Each commercial purpose issue indicate reason once suggest.",
            "image": "https://dummyimage.com/590x99",
            "subcategories": [
                {
                    "id": 58,
                    "name": "Gregory Meza",
                    "description": "Present administration western defense though value worry. Inside discuss property house experience. Ready policy my alone meeting carry energy.",
                    "image": None
                }
            ]
        },
        {
            "id": 2,
            "name": "grocery",
            "description": "home appliances etc.,",
            "image": "grocery.jpg",
            "subcategories": [
                {
                    "id": 59,
                    "name": "David Thompson",
                    "description": "Purpose make behavior everything politics no. Why PM recognize.\nAttention report painting professor. Computer study long common last sing stage surface. Three common treat state. No ready sing wish.",
                    "image": None
                }
            ]
        },
        {
            "id": 34,
            "name": "Christine Graham",
            "description": "Deep probably model lead. Give always yes tonight. Street beyond building herself line.",
            "image": "https://placekitten.com/733/255",
            "subcategories": [
                {
                    "id": 61,
                    "name": "Thomas Dodson",
                    "description": "Law blue step home. Perhaps current start total. About you health check social. Particularly establish room fact simple.",
                    "image": None
                }
            ]
        },
        {
            "id": 78,
            "name": "Rachel Scott",
            "description": "Reveal very design effect someone close fall. Property build never church.\nResult in act like fill. Read bring building field management those democratic. Special later sing TV study girl mind deal.",
            "image": "https://picsum.photos/358/605",
            "subcategories": [
                {
                    "id": 63,
                    "name": "Hannah Williams",
                    "description": "Executive somebody war. Send official start positive full staff.\nSame move drive image. North expert explain land up whether.",
                    "image": None
                }
            ]
        },
        {
            "id": 91,
            "name": "Timothy Arnold",
            "description": "Increase decide series talk federal. Rise care book modern second third.",
            "image": "https://dummyimage.com/238x424",
            "subcategories": [
                {
                    "id": 64,
                    "name": "Roger Jones",
                    "description": "Cold plan relate condition. Series listen them shake community local kind.\nSouth again admit remember along for space. Force agree claim face theory. Goal project than great something address sense.",
                    "image": None
                }
            ]
        },
        {
            "id": 81,
            "name": "Aaron Miller",
            "description": "Read since hard message western option. Operation have onto fill son.",
            "image": "https://placekitten.com/821/526",
            "subcategories": [
                {
                    "id": 66,
                    "name": "Tony Hoffman",
                    "description": "Course allow region. Environmental use other anything and traditional conference. Top then phone.\nAnyone politics world entire. Onto range partner business sense.",
                    "image": None
                },
                {
                    "id": 98,
                    "name": "Nathan Owen",
                    "description": "Because government finally. Center wide produce home full health.\nGood fly establish Democrat show civil. Campaign scientist consumer suffer partner should official. Material factor upon performance.",
                    "image": None
                }
            ]
        },
        {
            "id": 95,
            "name": "Katherine Beard",
            "description": "Suggest drive hundred unit trial natural. Mention act far development soldier.",
            "image": "https://picsum.photos/735/819",
            "subcategories": [
                {
                    "id": 68,
                    "name": "Aaron Vazquez",
                    "description": "Question particularly project morning newspaper account plant marriage. Including tonight outside today. Argue really significant risk and happen quality.",
                    "image": None
                }
            ]
        },
        {
            "id": 19,
            "name": "Bethany Johnston",
            "description": "Chair note free guy concern write able. Bit leg sound with student impact base blood.\nDefense white discuss evening large inside speech. Down although wear young. There culture cup north.",
            "image": "https://picsum.photos/706/667",
            "subcategories": [
                {
                    "id": 69,
                    "name": "Eugene Barr",
                    "description": "Guess anything indeed management theory. More recognize cold. We stuff early kid option.\nPrevent care effect later together job.\nItself capital agree. Performance every shoulder against.",
                    "image": None
                },
                {
                    "id": 74,
                    "name": "Michael Villa",
                    "description": "Democratic per record place. Stand old black middle hard technology surface then.\nWest sound seven instead second. Night step court doctor.",
                    "image": None
                }
            ]
        },
        {
            "id": 51,
            "name": "Rachel Mendoza",
            "description": "Evidence wrong allow throw community quite cost. Popular page industry face success adult. Player safe president system usually.",
            "image": "https://picsum.photos/270/524",
            "subcategories": [
                {
                    "id": 70,
                    "name": "Margaret Gomez",
                    "description": "Business lay scientist tend analysis. Which series level present until keep. Someone official red data. Travel hit less draw part.",
                    "image": None
                }
            ]
        },
        {
            "id": 58,
            "name": "Elaine Mayer",
            "description": "Need wrong your young. Reveal and push themselves course. Book knowledge area avoid government author tend.\nFund half success national. Prove shake late drive city everything view.",
            "image": "https://picsum.photos/262/166",
            "subcategories": [
                {
                    "id": 73,
                    "name": "Christine Kirk",
                    "description": "Field factor yet growth close. Something direction budget scene somebody result instead.\nForeign cultural now serious house. Prepare writer manager reduce law. Conference prepare grow item employee.",
                    "image": None
                },
                {
                    "id": 93,
                    "name": "Kelly Allen",
                    "description": "Forget open read feel record. Small center to action. Cut no or should season wait. Manage hit part window up structure write mission.",
                    "image": None
                }
            ]
        },
        {
            "id": 27,
            "name": "Amber Foster",
            "description": "Program help child gas appear exactly avoid. State author exist reality.\nHospital number detail interest policy. Record would hand theory guy issue. Deal situation doctor if south.",
            "image": "https://placekitten.com/766/975",
            "subcategories": [
                {
                    "id": 75,
                    "name": "Nicholas Williamson",
                    "description": "Story thought way among always. Technology simple partner age.\nHappen rather debate seek. So animal realize.",
                    "image": None
                }
            ]
        },
        {
            "id": 16,
            "name": "Steven Goodwin",
            "description": "Standard note thus Republican pattern. Rate important popular sort. Different live trade ago keep.\nExist company professor score discussion sell task.",
            "image": "https://picsum.photos/664/827",
            "subcategories": [
                {
                    "id": 78,
                    "name": "Dave Moore",
                    "description": "Physical society investment believe. Environment source certainly. Close chance crime our lose. Whether close thought respond probably car region.",
                    "image": None
                }
            ]
        },
        {
            "id": 89,
            "name": "Sabrina May",
            "description": "Realize serious bank bring anything. Wonder friend meet big group score.\nInto field off teacher upon identify series. Increase ahead look ready.",
            "image": "https://placekitten.com/602/516",
            "subcategories": [
                {
                    "id": 79,
                    "name": "Joy Moore",
                    "description": "Important upon huge gun product. Civil born television beyond heart.\nSeven bring hair find we eat group. Account summer grow likely real always campaign. Plan play a way political action.",
                    "image": None
                }
            ]
        },
        {
            "id": 82,
            "name": "Brenda Boyd",
            "description": "Memory hold baby choice wife range. World likely strategy check seem me.\nSafe foreign we option. Letter quite eye with nice while heavy page.",
            "image": "https://dummyimage.com/550x72",
            "subcategories": [
                {
                    "id": 81,
                    "name": "Mary Bauer",
                    "description": "Despite where discussion walk. Respond my government mind identify quite.\nDoor success purpose forget. Heart send style pretty something about. The may peace parent while trial.",
                    "image": None
                }
            ]
        },
        {
            "id": 66,
            "name": "Julie Keller",
            "description": "Room mother room myself less share bank relate. Between seat scene almost guess off town. Hard rise majority minute table. Recent south million southern partner.",
            "image": "https://picsum.photos/374/864",
            "subcategories": [
                {
                    "id": 82,
                    "name": "Emily Thomas",
                    "description": "Republican toward Mrs month. Need force test should condition along management.",
                    "image": None
                },
                {
                    "id": 94,
                    "name": "Mark Smith",
                    "description": "Explain indeed federal lay. Thing deep dinner us build receive.",
                    "image": None
                }
            ]
        },
        {
            "id": 96,
            "name": "George Fuller",
            "description": "Their today so security everybody. Every task any else travel. Herself race Congress world.\nPretty hard hit. Ask edge those street about drug.",
            "image": "https://picsum.photos/788/855",
            "subcategories": [
                {
                    "id": 83,
                    "name": "Alice Ayala",
                    "description": "Carry call particular what market identify. Strategy mean wide discussion want present.\nSeason evening letter character. Will base education course evening politics.",
                    "image": None
                }
            ]
        },
        {
            "id": 75,
            "name": "Jacob Humphrey",
            "description": "Property attention story yes. Plan event effect project but even begin. Everyone low four finish interesting.\nReturn fish military choice since. Apply price lot baby.",
            "image": "https://picsum.photos/214/67",
            "subcategories": [
                {
                    "id": 84,
                    "name": "Daniel Garza",
                    "description": "Actually present goal establish animal color. Probably vote evidence herself suffer music vote prevent. Cause quite late important choice how detail.",
                    "image": None
                }
            ]
        },
        {
            "id": 42,
            "name": "Mark Pope",
            "description": "Traditional truth edge sort. Little actually plan plan about ever read resource. Give energy professional alone open.\nFigure reveal woman million. Exist nice he study recent.",
            "image": "https://picsum.photos/857/394",
            "subcategories": [
                {
                    "id": 85,
                    "name": "Joseph Miranda",
                    "description": "Education yes its first leader center. Decision notice western team most green fact. Seem point individual set way central take. Quite design thank risk project senior the.",
                    "image": None
                }
            ]
        },
        {
            "id": 69,
            "name": "Mary Miller",
            "description": "Add project hotel will its serious. Consider defense note official through friend participant.",
            "image": "https://placekitten.com/411/466",
            "subcategories": [
                {
                    "id": 86,
                    "name": "Diane Zhang",
                    "description": "Call community story agent ball. Republican event budget author begin city often. Industry foot part care.",
                    "image": None
                },
                {
                    "id": 90,
                    "name": "Jerry Sutton",
                    "description": "Blood crime better professor accept air sister. Themselves choose these course effort above effort. Red perhaps within find whose. Talk that response.",
                    "image": None
                },
                {
                    "id": 91,
                    "name": "Brittany Downs",
                    "description": "Evidence watch any impact. Bed water box factor.\nServe budget know nothing thus water him. Study theory behind idea administration start represent. Born sport senior whether board their season.",
                    "image": None
                },
                {
                    "id": 101,
                    "name": "Felicia Contreras",
                    "description": "Lose major air. Me difference reveal simply never matter ahead practice. Guess hard series thus often provide know.",
                    "image": None
                }
            ]
        },
        {
            "id": 26,
            "name": "Gabriel Gomez",
            "description": "Score company apply although thus put home task.\nShake car book plant exist. Beautiful consider nice return apply consider article bring.",
            "image": "https://dummyimage.com/396x62",
            "subcategories": [
                {
                    "id": 87,
                    "name": "Christie Kelley",
                    "description": "Finish popular first. Choose heart best concern effect democratic.",
                    "image": None
                }
            ]
        },
        {
            "id": 14,
            "name": "Dr. Ashley Maxwell",
            "description": "Stay personal nothing police garden. Wife use we kind item yard note yard. Like only see red glass believe lose.",
            "image": "https://dummyimage.com/844x388",
            "subcategories": [
                {
                    "id": 92,
                    "name": "Linda Banks",
                    "description": "Everyone list eight window film. Nothing week attorney think bag either foot.\nDoctor age card worker might crime. Far beat inside information. Kitchen anyone response wrong example.",
                    "image": None
                }
            ]
        },
        {
            "id": 65,
            "name": "Angela Johnson",
            "description": "Unit write speak some behind clear dream. Address power effort.\nEat actually week country current able indeed economy. Coach marriage five boy design.",
            "image": "https://placekitten.com/953/209",
            "subcategories": [
                {
                    "id": 95,
                    "name": "Frank Coleman",
                    "description": "And occur possible task chair computer. Fear boy north return. Hot several while choose analysis final.\nMean early business audience ever moment. Market yes learn month.",
                    "image": None
                }
            ]
        },
        {
            "id": 97,
            "name": "Haley Smith",
            "description": "Sign customer hit into property land. Smile meeting program clear almost land. Of yourself education me. Result image they himself through impact picture soldier.",
            "image": "https://picsum.photos/141/748",
            "subcategories": [
                {
                    "id": 97,
                    "name": "Samuel Griffith",
                    "description": "Mention many forward already.\nVery listen clear major conference fund yourself. Thought stage popular instead tend. Off cup moment husband support.",
                    "image": None
                }
            ]
        },
        {
            "id": 85,
            "name": "Dwayne Griffith",
            "description": "Through study indicate enter decision occur design.\nSince shoulder sense policy son myself. Rest tree yet father hand inside certainly. Understand right admit along head anyone.",
            "image": "https://dummyimage.com/563x50",
            "subcategories": [
                {
                    "id": 99,
                    "name": "Ashley Carpenter",
                    "description": "Natural tax institution front red. Any onto heart indicate wife place send food.\nSee occur not really. Seat available maintain least choose measure reveal.",
                    "image": None
                }
            ]
        },
        {
            "id": 67,
            "name": "Tim Chavez",
            "description": "Energy nearly worker before guy consider per. Your air real toward individual example serious policy. Bit cost doctor poor.\nGreen bar quality mean.",
            "image": "https://dummyimage.com/524x565",
            "subcategories": [
                {
                    "id": 103,
                    "name": "Lisa Williams",
                    "description": "Health memory time her. Feeling agree military view understand boy.\nMagazine air ability a TV group. Possible agency free cost.",
                    "image": None
                }
            ]
        },
        {
            "id": 101,
            "name": "Tyler Foster",
            "description": "Newspaper attorney laugh reach their final music. Hand indicate commercial them.\nPresident enough them. Reflect detail star stop girl learn. Chance teach girl dinner dinner.",
            "image": "https://placekitten.com/715/772",
            "subcategories": []
        },
        {
            "id": 25,
            "name": "Donald Beck",
            "description": "Southern benefit help old my. Order car charge team call person worker change. Wait public include town social.",
            "image": "https://placekitten.com/203/71",
            "subcategories": []
        },
        {
            "id": 93,
            "name": "Heather Davidson",
            "description": "Game single west six. Ago leave evening determine. Approach reach color three low thank poor.\nMyself ever Mrs since. Individual true gun kind. Dark if gas entire provide actually relationship.",
            "image": "https://placekitten.com/824/991",
            "subcategories": []
        },
        {
            "id": 39,
            "name": "Morgan Brown",
            "description": "White condition sit operation picture letter. Suddenly interview can around try spend.",
            "image": "https://placekitten.com/775/989",
            "subcategories": []
        },
        {
            "id": 10,
            "name": "Karen Cohen",
            "description": "Learn tell lose teacher argue serious plan. Month themselves process TV too teacher. Fact fill entire policy.",
            "image": "https://dummyimage.com/252x83",
            "subcategories": []
        },
        {
            "id": 102,
            "name": "Daniel Young",
            "description": "House source finally trial go computer.\nEasy voice if foreign apply cold record sound. However difficult scientist including.\nWriter group each center blood. Live your bad but skin.",
            "image": "https://picsum.photos/54/548",
            "subcategories": []
        },
        {
            "id": 71,
            "name": "Aaron Adams",
            "description": "Increase recent operation walk bar month image speech. Movement believe religious behind most former red only.",
            "image": "https://placekitten.com/454/457",
            "subcategories": []
        },
        {
            "id": 72,
            "name": "Aaron Gordon",
            "description": "Ever break add agreement lead.\nBeautiful analysis pretty chair body.\nTrade able yet near walk tax. Difference as turn some smile.\nHome military skin author mouth price.",
            "image": "https://picsum.photos/401/107",
            "subcategories": []
        },
        {
            "id": 47,
            "name": "Andrew Franco",
            "description": "Receive inside box eight. Entire several yet line sense star stock.\nBut practice high bag left blue agency. Common middle health that natural once station series. Create model agree rather before.",
            "image": "https://picsum.photos/0/438",
            "subcategories": []
        },
        {
            "id": 15,
            "name": "Robert Reyes",
            "description": "Help no down force. Possible break history rich describe boy site.\nParty know rock. Hundred whatever Mr remain husband. Case character agent.",
            "image": "https://picsum.photos/456/379",
            "subcategories": []
        },
        {
            "id": 56,
            "name": "Alan Swanson",
            "description": "Wonder answer agree north too former expert. Team inside site skin anything.\nMilitary mind thing right. Cup watch its yard marriage. Former charge ever assume like Mr coach.",
            "image": "https://picsum.photos/69/980",
            "subcategories": []
        },
        {
            "id": 13,
            "name": "Michael Vargas",
            "description": "Road energy machine blue rest media usually. To market race sometimes order international bad yourself. News too deep enjoy agent.",
            "image": "https://picsum.photos/988/588",
            "subcategories": []
        },
        {
            "id": 21,
            "name": "Maureen Thomas",
            "description": "Light across such occur age player. Suddenly control people agent that.",
            "image": "https://dummyimage.com/258x19",
            "subcategories": []
        },
        {
            "id": 52,
            "name": "Russell Saunders",
            "description": "Pull single claim generation. Most order happen president turn although. Ready thing new.\nCondition across lead can do. Happy usually inside institution interest.",
            "image": "https://dummyimage.com/191x863",
            "subcategories": []
        },
        {
            "id": 100,
            "name": "Jon Mckee",
            "description": "Class not situation that. Degree throughout feel appear. Free fire better lose.\nAge attention himself apply improve. Collection fill human place group young fall. No position son then network out.",
            "image": "https://placekitten.com/545/794",
            "subcategories": []
        },
        {
            "id": 8,
            "name": "Anthony Campbell",
            "description": "Article history rate magazine across. Also poor human myself single. Ask statement clearly enter bad.",
            "image": "https://placekitten.com/740/611",
            "subcategories": []
        },
        {
            "id": 80,
            "name": "Jacob Roach DDS",
            "description": "One evidence low fall mention loss decision window. Election little around reflect. One fall provide southern discover matter.\nMother join able sound capital late per.",
            "image": "https://dummyimage.com/665x1013",
            "subcategories": []
        },
        {
            "id": 99,
            "name": "Michael Bryan",
            "description": "Theory economic science exactly. Always share expert bad.\nGeneral drop anyone hear specific man. Beyond between out.",
            "image": "https://dummyimage.com/106x710",
            "subcategories": []
        },
        {
            "id": 48,
            "name": "John Newton",
            "description": "Nearly citizen next easy yet move physical. Evening land trade majority. My one analysis particularly their city affect current.\nRecently shake feeling side.",
            "image": "https://dummyimage.com/460x751",
            "subcategories": []
        },
        {
            "id": 30,
            "name": "Frank Steele",
            "description": "Long up according name surface mind attack radio.\nBack first maintain language three court blood. Quite serve future any democratic reason.",
            "image": "https://placekitten.com/515/860",
            "subcategories": []
        },
        {
            "id": 76,
            "name": "Claire Williams",
            "description": "Yourself inside hold clearly event later foreign. Similar street watch enter region paper. Believe end possible network movie.",
            "image": "https://dummyimage.com/908x422",
            "subcategories": []
        },
        {
            "id": 6,
            "name": "Debbie Obrien",
            "description": "Per environment want risk more. Girl imagine could head. Republican crime avoid say share bar.\nEvent show identify bad. Exactly memory lead artist sound hot happen.",
            "image": "https://picsum.photos/716/788",
            "subcategories": []
        },
        {
            "id": 29,
            "name": "Andrew Anderson",
            "description": "Someone oil example good option trouble.\nLike force suddenly stop thousand four. Teach event like training year discover.",
            "image": "https://placekitten.com/736/233",
            "subcategories": []
        },
        {
            "id": 54,
            "name": "Patricia Taylor",
            "description": "Feel medical run turn successful. Shake oil various piece painting game. Near win strong ask suggest teacher.\nMethod him off section. Among first worry still like police.",
            "image": "https://picsum.photos/855/341",
            "subcategories": []
        },
        {
            "id": 103,
            "name": "James Miller",
            "description": "Plan three cover world level Congress her.\nAnalysis parent nor office author assume resource. Which community hot bad apply worry. Him reality grow black consider mission hard.",
            "image": "https://dummyimage.com/354x340",
            "subcategories": []
        },
        {
            "id": 53,
            "name": "Candice Garcia",
            "description": "System security quality suddenly accept blue part. Hospital everything no standard keep. Likely stop data.",
            "image": "https://dummyimage.com/272x21",
            "subcategories": []
        },
        {
            "id": 92,
            "name": "Emily Mathis",
            "description": "Argue born she significant gun care news by. Thank physical address ability large. Language success realize sing suffer collection together.",
            "image": "https://placekitten.com/627/329",
            "subcategories": []
        },
        {
            "id": 49,
            "name": "Jennifer Lee",
            "description": "Else break white fight. Kind positive night as yourself establish himself. Firm my prepare under blood woman can.",
            "image": "https://placekitten.com/857/784",
            "subcategories": []
        },
        {
            "id": 22,
            "name": "Eric Lane",
            "description": "Two rich and send service suggest world. Strong artist form. Plan beyond last TV high travel.\nUnderstand cut sit professional make build. Computer sense detail nothing issue.",
            "image": "https://dummyimage.com/383x431",
            "subcategories": []
        },
        {
            "id": 60,
            "name": "Brendan Evans",
            "description": "Focus main court evening agreement able decade garden. Event threat include move above space.\nListen structure yeah natural four appear money. Myself they check same difficult try senior law.",
            "image": "https://picsum.photos/522/177",
            "subcategories": []
        },
        {
            "id": 61,
            "name": "Alicia Compton",
            "description": "Yes attention rather they imagine inside play. Somebody how partner interesting present off.\nNever develop management amount human focus work. Imagine sure face line far rock blood.",
            "image": "https://placekitten.com/223/869",
            "subcategories": []
        },
        {
            "id": 35,
            "name": "Katrina Carter",
            "description": "Rich his know message. Section such stand.\nChoose appear receive. Time order month soon six.\nCharge issue area indeed raise new. Put around whole or station size.",
            "image": "https://dummyimage.com/783x959",
            "subcategories": []
        },
        {
            "id": 63,
            "name": "Hector Gallagher",
            "description": "Out face test father to clear society. Sign study church information.\nNorth within will her vote. Country boy affect big court. Audience until first world reduce state every. Analysis yet recently.",
            "image": "https://placekitten.com/734/616",
            "subcategories": []
        },
        {
            "id": 9,
            "name": "John Baxter",
            "description": "Quality poor collection represent say. Front key enter and. Production big example like.\nManage radio subject amount physical begin. When audience all billion.",
            "image": "https://placekitten.com/751/540",
            "subcategories": []
        }
    ],
    "message": "Data fetched successfully"
}
@app.route('/api/categories/', methods=['GET'])
def get_items():
    if request.method == "GET":
        return data

@app.route('/api/login/', methods=['POST'])
def login():
    login = False
    data = request.get_json()
    if(data['email'] == userdata['email']):
        login = True
    return jsonify(login)

@app.route('/api/register', methods = ['POST'])
def register():
    def isExist(data, email):
        for dict in data:
            if dict.get('email') == email:
                return True
        return False
    reqData = request.get_json()
    with open("accounts.json", "r") as file:
        read_data = json.load(file)
    if not isExist(read_data, reqData['email']):
        acc = {
            'email' : reqData['email'],
            'password' : reqData['password']
        }
        with open("accounts.json", "r") as file:
            daa = json.load(file)
        daa.append(acc)    
        with open("accounts.json", "w") as file:
            json.dump(daa, file, indent=2)
        return register_success
    return ({"status": "ERROR",
            "code": 910,
            "message": "Email Exist"})
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)


