minStamPot = 2
mobName = 'an ogre lord'

def getItemsFromButler():
    Mobiles.UseMobile(0x0007B97A)
    Gumps.WaitForGump(989312372, 10000)
    Gumps.SendAction(989312372, 4)
    Gumps.WaitForGump(989312372, 10000)
    Gumps.SendAction(989312372, 6)
    Misc.Pause(1000)
    
# Record your own restock macro
def restock():
    Items.UseItem(0x44481B36)
    Player.Run("East")
    Player.Run("East")
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 86)
    Misc.Pause(3500)
    Player.Run("North")
    Player.Run("North")
    Player.Run("North")
    Player.Run("North")
    Player.Run("North")
    Misc.Pause(1650)
    Player.Run("Right")
    Player.Run("Right")
    Player.Run("Right")
    while Items.BackpackCount( 0x0F0B ,-1 ) < minStamPot:
        getItemsFromButler()
    Items.UseItem(0x44481B36)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 56)
    Misc.Pause(4000)
    Dress.ChangeList('slayer')
    Dress.DressFStart()
    Misc.Pause(1000)
    
def checkForMobile():

    Player.Run('West')
    Player.Run('West')
    Player.Run('West')
    Player.Run('West')
    mobile = Mobiles.ApplyFilter(mobileFilter)
    if mobile:
        closest = Mobiles.Select(mobile, 'Nearest')
        Target.SetLast(closest)
        return closest

def treadMobile(mobile):
    mobilePosition = mobile.Position
    mobileCoords = PathFinding.Route()
    mobileCoords.MaxRetry = 2
    mobileCoords.StopIfStuck = False
    mobileCoords.IgnoreMobile = True
    mobileCoords.X = mobilePosition.X
    mobileCoords.Y = mobilePosition.Y
    stamPot()
    canGo = PathFinding.Go( mobileCoords )
    stamPot()
    
    
    
def stamPot():
    if Player.Stam < Player.StamMax:
        Items.UseItemByID(0x0F0B)
        Misc.Pause(500)
        
def panic():
    Player.HeadMessage(53, 'GET THE FUCK OUT OF HERE')
    Misc.Pause(500)
    Player.PathFindTo(1688, 2470, 30)
    Misc.Pause(2400)
    Player.HeadMessage(53, 'THIS WAY')
    Player.PathFindTo(1686, 2455, 30)
    Misc.Pause(2200)
    Player.UseSkill('Hiding')
    Misc.Pause(20000)
    
def waitForRecharge(num):
    currentHits = Player.Hits
    for x in range(num):
        if Player.Hits < currentHits:
            panic()
            break
        Misc.Pause(1000)
      
while True:
    if Items.BackpackCount( 0x0F0B ,-1 ) < minStamPot:
        restock()
    else:
        mobileFilter = Mobiles.Filter()
        mobileFilter.Name = mobName
        mobileFilter.RangeMin = 5
        Items.UseItemByID(0x0F0B)

        while True:
            mobile = None 
            for x in range(4):
                if mobile:
                    break
                else:
                    mobile = checkForMobile()
                        
            if mobile: 
                Misc.Pause(1000)
                Player.Attack(mobile)
                Misc.Pause(350)
                stamPot()
                if Player.DistanceTo(mobile) <= 2:
                    treadMobile(mobile)
                    break
                elif Player.DistanceTo(mobile) > 2 and Player.DistanceTo(mobile) <= 7:
                    break
            else:
                break       
       
        stamPot()
        Player.HeadMessage(55,'Avoiding Corners')
        Player.PathFindTo(1665, 2470, 41)
        Misc.Pause(600)
        Player.HeadMessage(55,'Going to Hide')
        Player.PathFindTo(1676, 2471, 41)
        Misc.Pause(2000)
        Player.UseSkill('Hiding')
        waitForRecharge(30)
        if not Player.Position.X == 1678 and Player.Position.Y == 2470 and Player.Position.Z == 40:
            Player.PathFindTo(1678, 2470, 40)
    
    



