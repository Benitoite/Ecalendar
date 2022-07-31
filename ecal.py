from datetime import datetime, timedelta;
import sys
import os

os.system("touch static/el1.html")
today = datetime.today()
electionday = datetime(2022, 11, 8, 0, 0, 0) 
diff = today - electionday
numdays = int(diff.days)

original_stdout = sys.stdout # Save a reference to the original standard output

with open('static/el1.html', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print('''
<!DOCTYPE html>
<html>
   <head>
      <title>E Calendar</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="refresh" content="3600" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

#wrap {
  width: 1000px;
  height: 70px;
  padding: 0;
  overflow: show;
}

#scaled-frame {
  width: 500px;
  height: 70px;
  border: 0px;
}

#scaled-frame {
  zoom: 3;
  -moz-transform: scale(2);
  -moz-transform-origin: 0 0;
  -o-transform: scale(2);
  -o-transform-origin: 0 0;
  -webkit-transform: scale(2);
  -webkit-transform-origin: 0 0;
}

@media screen and (-webkit-min-device-pixel-ratio:0) {
  #scaled-frame {
    zoom: 1;
  }
}
</style>   </head>
   <body style="font-family:Garamond;background-color:rgb(26, 0, 26);color:white;text-shadow: 
    0 1px 1px black, 
    0 2px 2px cyan;">''')
    
    print('<h1>Today is '+str(today.isoformat()[:10]))
    print('<div id="wrap" style="position:absolute; top: 0px; right: 2px;"><iframe id="scaled-frame"   frameBorder="0" src="https://17230.ddns.net/static/pac.html"></iframe></div>')
    
    print('<center><h1 style="text-shadow:0 0 1px black,0 5px 10px black,0 10px 20px cyan;font-family:Helvetica;font-size:255px;">')
    
    if numdays < 0: 
      print('E '+str(numdays))
    if numdays == 0:
      print('E 0 ... Election Day')
    if numdays > 0:
      print('E +'+str(numdays))
            
    print('</h1><font size=3></center>')

    if (numdays == -125):
      print('<hr><h1 style="font-size:24px;">RESOLUTIONS TO BE SUBMITTED TO THE ROV (E- 125)<p><h2 style="font-size:18px;">Date for jurisdictions to submit resolutions calling for a candidate election to meet timeline for a full nomination period. The ROV encourages jurisdictions to provide a resolution as early as possible.')

    if (numdays == -113):
      print('<hr><h1 style="font-size:24px;">NOMINATION PERIOD OPENS (E- 113)<p><h2 style="font-size:18px;">First day candidates may pick up nomination documents at the office of the Registrar of Voters')

    if (numdays >= -103) & (numdays <= -88):
      print('<hr><h1 style="font-size:24px;">PERIOD FOR MEASURE RESOLUTIONS AND TAX RATE STATEMENTS TO BE SUBMITTED TO THE ROV (E- 103 to 88)<p><h2 style="font-size:18px;">Between these dates is the period for jurisdictions to submit a resolution calling for a measure election, and if applicable, tax rate statements. The ROV encourages jurisdictions to provide a resolution as early as possible.')

    if (numdays >= -90) & (numdays <= 0):
      print('<hr><h1 style="font-size:24px;">CONTRIBUTION / INDEPENDENT EXPENDITURES (E- 90 to 0)<p><h2 style="font-size:18px;">Sums of $1,000 or more to/from a single source must be reported within 24-hours. The Independent Expenditure report is required only for committees (not candidate controlled) that make independent expenditures totaling $1,000 or more to support or oppose a single ballot measure or a single candidate.')

    if (numdays == -88):
      print('<hr><h1 style="font-size:24px;">NOMINATION PERIOD CLOSES (E- 88)<p><h2 style="font-size:18px;">Deadline to file (in the Office of the Registrar of Voters only) all required nomination documents.')

    if (numdays == -88):
      print('<hr><h1 style="font-size:24px;">LAST DAY FOR PROPONENTS TO WITHDRAW AN INITIATIVE (E- 88)<p><h2 style="font-size:18px;">Last day for proponents to withdraw an initiative that qualified for the ballot.')

    if (numdays >= -87) & (numdays <= -83):
      print('<hr><h1 style="font-size:24px;">NOMINATION EXTENSION PERIOD (E- 87 to 83)<p><h2 style="font-size:18px;">If the incumbent fails to file a Declaration of Candidacy by deadline for their office, there will be a 5-calendar-day extension during which any candidate, other than the incumbent, may file for said office.')

    if (numdays == -84):
      print('<hr><h1 style="font-size:24px;">DUE DATE FOR PRIMARY ARGUMENTS (E- 84)<p><h2 style="font-size:18px;">5:00 p.m. is the deadline set by the Registrar of Voters for submitting primary arguments in favor of and against a measure. Arguments for City measures must be filed with the City Clerk\'s office. Contact the City Clerk\'s office for filing deadlines.')

    if (numdays == -83):
      print('<hr><h1 style="font-size:24px;">LAST DAY TO AMEND OR WITHDRAW A MEASURE (E- 83)<p><h2 style="font-size:18px;">Deadline for jurisdictions to amend or withdraw a measure from the ballot. The measure must be amended or withdrawn by resolution. ')

    if (numdays >= -83) & (numdays <= -74):
      print('<hr><h1 style="font-size:24px;">EXAMINATION PERIOD FOR ALL PRIMARY ARGUMENTS FILED<p><h2 style="font-size:18px;">The elections official shall make the arguments available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

    if (numdays == -82):
      print('<hr><h1 style="font-size:24px;">RANDOMIZED ALPHABET DRAWING (E- 82)<p><h2 style="font-size:18px;">This day the Secretary of State (SOS) and the local elections official will conduct a drawing of letters of the alphabet to determine the order in which candidates appear on the ballot. For local offices, candidates should refer to the SOS\'s drawing, and for State or Legislative offices, candidates should refer to the ROV\'s drawing for order of their name to appear on the ballot. ')

    if (numdays == -77):
      print('<hr><h1 style="font-size:24px;">DUE DATE FOR REBUTTAL ARGUMENTS AND IMPARTIAL ANALYSES (E- 77)<p><h2 style="font-size:18px;">Deadline set by the Registrar of Voters for submitting rebuttal arguments to primary arguments in favor of and against a measure and impartial analyses.')

    if (numdays >= -76) & (numdays <= -67):
      print('<hr><h1 style="font-size:24px;">EXAMINATION PERIOD FOR ALL REBUTTALS AND IMPARTIAL ANALYSES FILED (E- 76 to 67)<p><h2 style="font-size:18px;">The elections official shall make the rebuttal arguments and Impartial Analyses available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

    if (numdays == -67):
      print('<hr><h1 style="font-size:24px;">FINAL PRINTING DEADLINE (E- 67)<p><h2 style="font-size:18px;">Any petition for writ of mandate, including any appeals, should be resolved by this date so the Registrar of Voters can meet necessary printing deadlines')

    if (numdays >= -57) & (numdays <= -14):
      print('<hr><h1 style="font-size:24px;">WRITE-IN CANDIDACY PERIOD (E- 57 to 14)<p><h2 style="font-size:18px;">Between these dates is the period for candidates to obtain and file write-in nomination documents in the Office of the Registrar of Voters.')

    if (numdays == -40):
      print('<hr><h1 style="font-size:24px;">F.P.P.C. 1 st PRE-ELECTION STATEMENT DUE (E- 40)<p><h2 style="font-size:18px;">Deadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed<p><h3>Reporting Period: July 1, 2022 to September 24, 2022')

    if (numdays == -29):
      print('<hr><h1 style="font-size:24px;">FIRST DAY TO BEGIN MAILING VOTE-BY-MAIL BALLOTS (E- 29)<p><h2 style="font-size:18px;">First day to begin mailing vote-by-mail ballots')

    if (numdays >= -29) & (numdays <= -1):
      print('\EARLY VOTING PERIOD AT THE ROV OFFICE (E- 29 to 1)<p><h2 style="font-size:18px;">Early voting is available at the Registrar of Voters office for individuals wishing to drop off ballot or vote in person during normal business hours, Monday through Friday, 8:00 a.m. to 5:00 p.m., beginning 29 days prior the election.')

    if (numdays == -15):
      print('<hr><h1 style="font-size:24px;">LAST DAY TO REGISTER TO VOTE FOR JUNE ELECTION (E- 15)<p><h2 style="font-size:18px;">Deadline to register to be eligible to vote in this election.')

    if (numdays == -12):
      print('<hr><h1 style="font-size:24px;">F.P.P.C. 2 nd PRE-ELECTION STATEMENT DUE (E- 12)<p><h2 style="font-size:18px;">Deadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.<p><h3>Reporting Period: September 25, 2022 to October 22, 2022')

    if (numdays >= -10) & (numdays <= 0):
      print('\VOTE CENTERS OPEN 10 DAYS BEFORE ELECTION DAY (E- 10 to 0)<p><h2 style="font-size:18px;">Vote Centers are open to all registered voters in Santa Clara County. Vote Centers are open to all registered voters in jurisdictions holding special elections. Any voter can go to any Vote Center location throughout the County. Hours may vary by location and locations may vary with each election – please see listing on our website at sccvote.com')

    if (numdays >= -14) & (numdays <= 0):
      print('\CONDITIONAL VOTER REGISTRATION (E- 14 to 0)<p><h2 style="font-size:18px;">Conditional Voter Registration is open for a full 14 days prior to the election and must be done in person at the Registrar of Voters office or at any Vote Center. Vote centers are open 11 days prior to the election. Vote centers hours of operations my vary. Please check our website for the latest information.')

    if (numdays == -7):
      print('<hr><h1 style="font-size:24px;">LAST DAY TO REQUEST VOTE-BY-MAIL BALLOT TO BE MAILED (E- 7)<p><h2 style="font-size:18px;">Deadline at 5:00 p.m. to submit a request for a Vote-by-Mail ballot to be mailed to voter.')

    if (numdays == 0):
      print('<hr><h1 style="font-size:24px;">ELECTION DAY (E 0)<p><h2 style="font-size:18px;">All Vote Centers and ROV office are open from 7:00 a.m. to 8:00 p.m. for dropping off ballot or voting in person. Ballots must be postmarked by this date to ensure eligibility of counted votes.')

    if (numdays == 22):
      print('<hr><h1 style="font-size:24px;">ELECTIONS OFFICIAL TO NOTIFY VOTER OF VERIFICATION OF SIGNATURE (E+ 22)<p><h2 style="font-size:18px;">In the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

    if (numdays == 28):
      print('<hr><h1 style="font-size:24px;">SIGNATURE VERIFICATION DATE (E+ 28)<p><h2 style="font-size:18px;">Last day to turn in unsigned ballots or signature verification statements.')

    if (numdays == 30):
      print('<hr><h1 style="font-size:24px;">OFFICIAL CANVASS OF VOTE (E+ 30)<p><h2 style="font-size:18px;">n the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

    if (numdays == 84):
      print('<hr><h1 style="font-size:24px;">F.P.P.C. SEMI-ANNUAL STATEMENT DUE (E+ 84)<p><h2 style="font-size:18px;">Deadline for semi-annual financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.<p><h3>Reporting Period: July 1, 2022 to December 31, 2022')

    print('''</body></html>''')
    sys.stdout = original_stdout # Reset the standard output to its original value
