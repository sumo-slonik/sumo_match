from club_competitor import ClubCompetotor
from personal_competitor import PersonalCompetitor





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    competitor1 = PersonalCompetitor("kuba nowakowski","Luks Lubzina",103,100,2000)
    competitor2 = PersonalCompetitor("Maciek nowakowski", "Luks Lubzina", 93, 92, 2000)
    competitor3 = PersonalCompetitor("Inny nowakowski", "Luks Lubzina", 93, 92, 2000)
    competitor4 = PersonalCompetitor("kolejny nowakowski", "Luks Lubzina", 93, 92, 2000)
    teem = ClubCompetotor(competitor1,competitor2,competitor3,competitor4,"Luks Lubzina")
    print(teem.get_firs_competitor().get_first_name())
    teem.use_substitute(1)
    print(teem.get_firs_competitor().get_first_name())
    teem.use_substitute(1)
    print(teem.get_firs_competitor().get_first_name())