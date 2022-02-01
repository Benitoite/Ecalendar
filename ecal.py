from datetime import datetime, timedelta
import sys


today = datetime.today() -  timedelta(hours=8)
electionday = datetime(2022, 6, 7, 0, 0, 0)  - timedelta(hours=8) 
diff = today - electionday
numdays = int(diff.days)



original_stdout = sys.stdout # Save a reference to the original standard output

with open('el.html', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.


    print('<h1>Today is '+str(today.isoformat()[:10]))

    if numdays < 0: 
      print('<center><font size=7><h1>E '+str(numdays)+'</h1><font size=3></center>')
    if numdays == 0:
      print('<center><font size=7><h1>E '+str(numdays)+'</h1><font size=3></center>')
    if numdays > 0:
      print('<center><font size=7><h1>E +'+str(numdays)+'</h1><font size=3></center>')

    if (numdays >= -155) & (numdays <= -118):
      print('<hr><h1>SIGNATURES IN LIEU OF FILING FEE PERIOD (E- 155 to 118)<p><h2>All state and county offices (except for Board of Supervisors) for which there is a filing fee')

    if (numdays >= -147) & (numdays <= -118):
      print('<hr><h1>SIGNATURES IN LIEU OF FILING FEE PERIOD (E- 147 to 118)<p><h2>All Board of Supervisors offices for which there is a filing fee.')

    if (numdays >= -127) & (numdays <= -118):
      print('<hr><h1>DECLARATION OF INTENTION PERIOD (E- 127 to 118)<p><h2>Judicial offices only. Incumbents must file during this period.')

    if (numdays == -125):
      print('<hr><h1>RESOLUTIONS TO BE SUBMITTED TO THE ROV (E- 125)<p><h2>Date for jurisdictions to submit resolutions calling for a candidate election to meet timeline for a full nomination period. The ROV encourages jurisdictions to provide a resolution as early as possible.')

    if (numdays >= -117) & (numdays <= -113):
      print('<hr><h1>DECLARATION OF INTENTION EXTENSION PERIOD (E- 117 to 113)<p><h2>If the incumbent judge has not filed a Declaration of Intention to succeed to the same office, then any other person, other than the incumbent, may file such a declaration during the extension period.')

    if (numdays == -113):
      print('<hr><h1>NOMINATION PERIOD OPENS (E- 113)<p><h2>First day candidates may pick up nomination documents at the office of the Registrar of Voters')

    if (numdays >= -103) & (numdays <= -88):
      print('<hr><h1>PERIOD FOR MEASURE RESOLUTIONS AND TAX RATE STATEMENTS TO BE SUBMITTED TO THE ROV (E- 103 to 88)<p><h2>Between these dates is the period for jurisdictions to submit a resolution calling for a measure election, and if applicable, tax rate statements. The ROV encourages jurisdictions to provide a resolution as early as possible.')

    if (numdays >= -90) & (numdays <= 0):
      print('<hr><h1>CONTRIBUTION / INDEPENDENT EXPENDITURES (E- 90 to 0)<p><h2>Sums of $1,000 or more to/from a single source must be reported within 24-hours. The Independent Expenditure report is required only for committees (not candidate controlled) that make independent expenditures totaling $1,000 or more to support or oppose a single ballot measure or a single candidate.')

    if (numdays == -88):
      print('<hr><h1>NOMINATION PERIOD CLOSES (E- 88)<p><h2>Deadline to file (in the Office of the Registrar of Voters only) all required nomination documents.')

    if (numdays >= -87) & (numdays <= -83):
      print('<hr><h1>NOMINATION EXTENSION PERIOD (E- 87 to 83)<p><h2>If the incumbent fails to file a Declaration of Candidacy by deadline for their office, there will be a 5-calendar-day extension during which any candidate, other than the incumbent, may file for said office.')

    if (numdays == -84):
      print('<hr><h1>DUE DATE FOR PRIMARY ARGUMENTS (E- 84)<p><h2>5:00 p.m. is the deadline set by the Registrar of Voters for submitting primary arguments in favor of and against a measure. Arguments for City measures must be filed with the City Clerk\'s office. Contact the City Clerk\'s office for filing deadlines.')

    if (numdays == -83):
      print('<hr><h1>LAST DAY TO AMEND OR WITHDRAW A MEASURE (E- 83)<p><h2>Deadline for jurisdictions to amend or withdraw a measure from the ballot. The measure must be amended or withdrawn by resolution. ')

    if (numdays >= -83) & (numdays <= -74):
      print('<hr><h1>EXAMINATION PERIOD FOR ALL PRIMARY ARGUMENTS FILED<p><h2>The elections official shall make the arguments available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

    if (numdays == -82):
      print('<hr><h1>RANDOMIZED ALPHABET DRAWING (E- 82)<p><h2>This day the Secretary of State (SOS) and the local elections official will conduct a drawing of letters of the alphabet to determine the order in which candidates appear on the ballot. For local offices, candidates should refer to the SOS\'s drawing, and for State or Legislative offices, candidates should refer to the ROV\'s drawing for order of their name to appear on the ballot. ')

    if (numdays == -77):
      print('<hr><h1>DUE DATE FOR REBUTTAL ARGUMENTS AND IMPARTIAL ANALYSES (E- 77)<p><h2>Deadline set by the Registrar of Voters for submitting rebuttal arguments to primary arguments in favor of and against a measure and impartial analyses.')

    if (numdays >= -76) & (numdays <= -67):
      print('<hr><h1>EXAMINATION PERIOD FOR ALL REBUTTALS AND IMPARTIAL ANALYSES FILED (E- 76 to 67)<p><h2>The elections official shall make the rebuttal arguments and Impartial Analyses available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

    if (numdays == -67):
      print('<hr><h1>FINAL PRINTING DEADLINE (E- 67)<p><h2>Any petition for writ of mandate, including any appeals, should be resolved by this date so the Registrar of Voters can meet necessary printing deadlines')

    if (numdays >= -57) & (numdays <= -14):
      print('<hr><h1>WRITE-IN CANDIDACY PERIOD (E- 57 to 14)<p><h2>Between these dates is the period for candidates to obtain and file write-in nomination documents in the Office of the Registrar of Voters.')

    if (numdays == -40):
      print('<hr><h1>F.P.P.C. 1 st PRE-ELECTION STATEMENT DUE (E- 40)<p><h2>Deadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed<p><h3>Reporting Period: January 1, 2022 to April 23, 2022')

    if (numdays == -29):
      print('<hr><h1>FIRST DAY TO BEGIN MAILING VOTE-BY-MAIL BALLOTS (E- 29)<p><h2>First day to begin mailing vote-by-mail ballots')

    if (numdays >= -29) & (numdays <= -1):
      print('\EARLY VOTING PERIOD AT THE ROV OFFICE (E- 29 to 1)<p><h2>Early voting is available at the Registrar of Voters office for individuals wishing to drop off ballot or vote in person during normal business hours, Monday through Friday, 8:00 a.m. to 5:00 p.m., beginning 29 days prior the election.')

    if (numdays == -15):
      print('<hr><h1>LAST DAY TO REGISTER TO VOTE FOR JUNE ELECTION (E- 15)<p><h2>Deadline to register to be eligible to vote in this election.')

    if (numdays == -12):
      print('<hr><h1>F.P.P.C. 2 nd PRE-ELECTION STATEMENT DUE (E- 12)<p><h2>Deadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.<p><h3>Reporting Period: April 24, 2022 May 21, 2022')

    if (numdays >= -29) & (numdays <= 0):
      print('\VOTE CENTERS OPEN 10 DAYS BEFORE ELECTION DAY (E- 10 to 0)<p><h2>Vote Centers are open to all registered voters in Santa Clara County. Vote Centers are open to all registered voters in jurisdictions holding special elections. Any voter can go to any Vote Center location throughout the County. Hours may vary by location and locations may vary with each election – please see listing on our website at sccvote.com')

    if (numdays == -7):
      print('<hr><h1>LAST DAY TO REQUEST VOTE-BY-MAIL BALLOT TO BE MAILED (E- 7)<p><h2>Deadline at 5:00 p.m. to submit a request for a Vote-by-Mail ballot to be mailed to voter.')

    if (numdays == 0):
      print('<hr><h1>ELECTION DAY (E 0)<p><h2>All Vote Centers and ROV office are open from 7:00 a.m. to 8:00 p.m. for dropping off ballot or voting in person. Ballots must be postmarked by this date to ensure eligibility of counted votes.')

    if (numdays == 22):
      print('<hr><h1>ELECTIONS OFFICIAL TO NOTIFY VOTER OF VERIFICATION OF SIGNATURE (E+ 22)<p><h2>In the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

    if (numdays == 28):
      print('<hr><h1>SIGNATURE VERIFICATION DATE (E+ 28)<p><h2>Last day to turn in unsigned ballots or signature verification statements.')

    if (numdays == 30):
      print('<hr><h1>OFFICIAL CANVASS OF VOTE (E+ 30)<p><h2>n the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

    if (numdays == 55):
      print('<hr><h1>F.P.P.C. SEMI-ANNUAL STATEMENT DUE (E+ 55)<p><h2>Deadline for semi-annual financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.<p><h3>Reporting Period: January 1, 2022 to June 30, 2022')

    sys.stdout = original_stdout # Reset the standard output to its original value
