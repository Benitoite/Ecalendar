from datetime import datetime, timedelta

today = datetime.today() -  timedelta(hours=8)
electionday = datetime(2022, 6, 7, 0, 0, 0)  - timedelta(hours=8) 
diff = today - electionday
numdays = int(diff.days)
print('Today is '+str(today))

if numdays < 0: 
  print('E '+str(numdays))
if numdays == 0:
  print('E '+str(numdays))
if numdays > 0:
  print('E +'+str(numdays))

if (numdays >= -155) & (numdays <= -118):
  print('\tSIGNATURES IN LIEU OF FILING FEE PERIOD (E- 155 to 118)\n\t\tAll state and county offices (except for Board of Supervisors) for which there is a filing fee')

if (numdays >= -147) & (numdays <= -118):
  print('\tSIGNATURES IN LIEU OF FILING FEE PERIOD (E- 147 to 118)\n\t\tAll Board of Supervisors offices for which there is a filing fee.')

if (numdays >= -127) & (numdays <= -118):
  print('\tDECLARATION OF INTENTION PERIOD (E- 127 to 118)\n\t\tJudicial offices only. Incumbents must file during this period.')
   
if (numdays == -125):
  print('\tRESOLUTIONS TO BE SUBMITTED TO THE ROV (E- 125)\n\t\tDate for jurisdictions to submit resolutions calling for a candidate election to meet timeline for a full nomination period. The ROV encourages jurisdictions to provide a resolution as early as possible.')

if (numdays >= -117) & (numdays <= -113):
  print('\tDECLARATION OF INTENTION EXTENSION PERIOD (E- 117 to 113)\n\t\tIf the incumbent judge has not filed a Declaration of Intention to succeed to the same office, then any other person, other than the incumbent, may file such a declaration during the extension period.')

if (numdays == -113):
  print('\tNOMINATION PERIOD OPENS (E- 113)\n\t\tFirst day candidates may pick up nomination documents at the office of the Registrar of Voters')

if (numdays >= -103) & (numdays <= -88):
  print('\tPERIOD FOR MEASURE RESOLUTIONS AND TAX RATE STATEMENTS TO BE SUBMITTED TO THE ROV (E- 103 to 88)\n\t\tBetween these dates is the period for jurisdictions to submit a resolution calling for a measure election, and if applicable, tax rate statements. The ROV encourages jurisdictions to provide a resolution as early as possible.')

if (numdays >= -90) & (numdays <= 0):
  print('\tCONTRIBUTION / INDEPENDENT EXPENDITURES (E- 90 to 0)\n\t\tSums of $1,000 or more to/from a single source must be reported within 24-hours. The Independent Expenditure report is required only for committees (not candidate controlled) that make independent expenditures totaling $1,000 or more to support or oppose a single ballot measure or a single candidate.')

if (numdays == -88):
  print('\tNOMINATION PERIOD CLOSES (E- 88)\n\t\tDeadline to file (in the Office of the Registrar of Voters only) all required nomination documents.\n\tLAST DAY FOR PROPONENTS TO WITHDRAW AN INITIATIVE (E- 88)\n\t\tLast day for proponents to withdraw an initiative that qualified for the ballot.')

if (numdays >= -87) & (numdays <= -83):
  print('\tNOMINATION EXTENSION PERIOD (E- 87 to 83)\n\t\tIf the incumbent fails to file a Declaration of Candidacy by deadline for their office, there will be a 5-calendar-day extension during which any candidate, other than the incumbent, may file for said office.')

if (numdays == -84):
  print('\tDUE DATE FOR PRIMARY ARGUMENTS (E- 84)\n\t\t5:00 p.m. is the deadline set by the Registrar of Voters for submitting primary arguments in favor of and against a measure. Arguments for City measures must be filed with the City Clerk\'s office. Contact the City Clerk\'s office for filing deadlines.')

if (numdays == -83):
  print('\tLAST DAY TO AMEND OR WITHDRAW A MEASURE (E- 83)\n\t\tDeadline for jurisdictions to amend or withdraw a measure from the ballot. The measure must be amended or withdrawn by resolution. ')

if (numdays >= -83) & (numdays <= -74):
  print('\tEXAMINATION PERIOD FOR ALL PRIMARY ARGUMENTS FILED\n\t\tThe elections official shall make the arguments available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

if (numdays == -82):
  print('\tRANDOMIZED ALPHABET DRAWING (E- 82)\n\t\tThis day the Secretary of State (SOS) and the local elections official will conduct a drawing of letters of the alphabet to determine the order in which candidates appear on the ballot. For local offices, candidates should refer to the SOS\'s drawing, and for State or Legislative offices, candidates should refer to the ROV\'s drawing for order of their name to appear on the ballot. ')

if (numdays == -77):
  print('\tDUE DATE FOR REBUTTAL ARGUMENTS AND IMPARTIAL ANALYSES (E- 77)\n\t\tDeadline set by the Registrar of Voters for submitting rebuttal arguments to primary arguments in favor of and against a measure and impartial analyses.')

if (numdays >= -76) & (numdays <= -67):
  print('\tEXAMINATION PERIOD FOR ALL REBUTTALS AND IMPARTIAL ANALYSES FILED (E- 76 to 67)\n\t\tThe elections official shall make the rebuttal arguments and Impartial Analyses available for public examination during business hours for a period of 10-calendar days immediately following the filing deadline for submission of those documents.')

if (numdays == -67):
  print('\tFINAL PRINTING DEADLINE (E- 67)\n\t\tAny petition for writ of mandate, including any appeals, should be resolved by this date so the Registrar of Voters can meet necessary printing deadlines')

if (numdays >= -57) & (numdays <= -14):
  print('\tWRITE-IN CANDIDACY PERIOD (E- 57 to 14)\n\t\tBetween these dates is the period for candidates to obtain and file write-in nomination documents in the Office of the Registrar of Voters.')

if (numdays == -40):
  print('\tF.P.P.C. 1 st PRE-ELECTION STATEMENT DUE (E- 40)\n\t\tDeadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed\n\t\t\tReporting Period: January 1, 2022 to April 23, 2022')

if (numdays == -29):
  print('\tFIRST DAY TO BEGIN MAILING VOTE-BY-MAIL BALLOTS (E- 29)\n\t\tFirst day to begin mailing vote-by-mail ballots')

if (numdays >= -29) & (numdays <= -1):
  print('\EARLY VOTING PERIOD AT THE ROV OFFICE (E- 29 to 1)\n\t\tEarly voting is available at the Registrar of Voters office for individuals wishing to drop off ballot or vote in person during normal business hours, Monday through Friday, 8:00 a.m. to 5:00 p.m., beginning 29 days prior the election.')

if (numdays == -15):
  print('\tLAST DAY TO REGISTER TO VOTE FOR JUNE ELECTION (E- 15)\n\t\tDeadline to register to be eligible to vote in this election.')

if (numdays == -12):
  print('\tF.P.P.C. 2 nd PRE-ELECTION STATEMENT DUE (E- 12)\n\t\tDeadline for financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.\n\t\t\tReporting Period: April 24, 2022 May 21, 2022')

if (numdays >= -29) & (numdays <= 0):
  print('\VOTE CENTERS OPEN 10 DAYS BEFORE ELECTION DAY (E- 10 to 0)\n\t\tVote Centers are open to all registered voters in Santa Clara County. Vote Centers are open to all registered voters in jurisdictions holding special elections. Any voter can go to any Vote Center location throughout the County. Hours may vary by location and locations may vary with each election – please see listing on our website at sccvote.com')

if (numdays == -7):
  print('\tLAST DAY TO REQUEST VOTE-BY-MAIL BALLOT TO BE MAILED (E- 7)\n\t\tDeadline at 5:00 p.m. to submit a request for a Vote-by-Mail ballot to be mailed to voter.')

if (numdays == 0):
  print('\tELECTION DAY (E 0)\n\t\tAll Vote Centers and ROV office are open from 7:00 a.m. to 8:00 p.m. for dropping off ballot or voting in person. Ballots must be postmarked by this date to ensure eligibility of counted votes.')

if (numdays == 22):
  print('\tELECTIONS OFFICIAL TO NOTIFY VOTER OF VERIFICATION OF SIGNATURE (E+ 22)\n\t\tIn the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

if (numdays == 28):
  print('\tSIGNATURE VERIFICATION DATE (E+ 28)\n\t\tLast day to turn in unsigned ballots or signature verification statements.')

if (numdays == 30):
  print('\tOFFICIAL CANVASS OF VOTE (E+ 30)\n\t\tn the case of a voter whose signature does not match or is missing, the elections official is required to notify the voter at least 8 days before the certification of the election of an opportunity to update the voter\'s signature.')

if (numdays == 55):
  print('\tF.P.P.C. SEMI-ANNUAL STATEMENT DUE (E+ 55)\n\t\tDeadline for semi-annual financial disclosure report Form 460 covering the reporting period noted below or the day after the closing date of the last statement filed.\n\t\t\tReporting Period: January 1, 2022 to June 30, 2022')
