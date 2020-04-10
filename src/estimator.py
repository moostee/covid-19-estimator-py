import math;
import json;

def estimator(data):

  reportedCases = data['reportedCases']
  periodType = data['periodType']
  timeToElapse = data['timeToElapse']
  availableHospitalBeds = math.trunc(0.35 * data['totalHospitalBeds'])
  avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
  avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
  totalDailyIncomeInUSD = avgDailyIncomeInUSD * avgDailyIncomePopulation
  impactCurrentlyInfected, severeImpactCurrentlyInfected = CalculateCurrentlyInfected(reportedCases)  
  timeToElapse = getDays(periodType, timeToElapse)
  impactInfections, severeImpactInfections = getInfectionsByRequestedTime(impactCurrentlyInfected, severeImpactCurrentlyInfected, timeToElapse)
  impactSevereCases, severeImpactSevereCases = getSevereCasesByRequestedTime(impactInfections, severeImpactInfections)
  impactHospitalBeds,severeImpactHospitalBeds = getHospitalBedsByRequestedTime(impactSevereCases, severeImpactSevereCases,availableHospitalBeds)
  impactCasesForICU,severeImpactCasesForICU = getCasesForICUByRequestedTime(impactInfections, severeImpactInfections)
  impactCasesForVentilators,severeImpactCasesForVentilators = getCasesForVentilatorsByRequestedTime(impactInfections, severeImpactInfections)
  impactDollarInFlight, severeImpactDollarInFlight = getDollarInflight(impactInfections, severeImpactInfections,totalDailyIncomeInUSD, timeToElapse)
  impactData = getData(impactCurrentlyInfected, impactInfections, impactSevereCases, impactHospitalBeds, impactCasesForICU, impactCasesForVentilators, impactDollarInFlight,severeImpactCurrentlyInfected, severeImpactInfections, severeImpactSevereCases, severeImpactHospitalBeds, severeImpactCasesForICU, severeImpactCasesForVentilators, severeImpactDollarInFlight, False)
  severeImpactData = getData(impactCurrentlyInfected, impactInfections, impactSevereCases, impactHospitalBeds, impactCasesForICU, impactCasesForVentilators, impactDollarInFlight,severeImpactCurrentlyInfected, severeImpactInfections, severeImpactSevereCases, severeImpactHospitalBeds, severeImpactCasesForICU, severeImpactCasesForVentilators, severeImpactDollarInFlight, True)

  return json.dumps({
    "data" : data,
    "impact" : impactData,
    "severeImpact" : severeImpactData
  },indent = 2)

def CalculateCurrentlyInfected(reportedCases):
  impact = reportedCases * 10;
  severeImpact = reportedCases * 50;
  return impact, severeImpact

def getDays(periodType, timeToElapse) : 
  if periodType == 'days':
    return timeToElapse
  if periodType == 'weeks' : 
    return timeToElapse * 7  
  if periodType == 'months':
    return timeToElapse * 30
  
def getInfectionsByRequestedTime(impactCurrentlyInfected, severeImpactCurrentlyInfected, timeToElapse):
  factorial = math.trunc(timeToElapse // 3)
  impactInfections = math.trunc(impactCurrentlyInfected * (2**factorial))
  severeImpactInfections = math.trunc(severeImpactCurrentlyInfected * (2**factorial))
  return impactInfections, severeImpactInfections

def getSevereCasesByRequestedTime(impactRequestedTime, severeImpactRequestedTime):
  impactSevereCases = math.trunc(0.15 * impactRequestedTime)
  severeImpactSevereCases = math.trunc(0.15 * severeImpactRequestedTime)
  return impactSevereCases, severeImpactSevereCases

def getHospitalBedsByRequestedTime(impactSevereCases, severeImpactSevereCases, availableHospitalBeds):
  impactHospitalBeds = availableHospitalBeds - impactSevereCases
  severeImpactHospitalBeds = availableHospitalBeds - severeImpactSevereCases
  return impactHospitalBeds,severeImpactHospitalBeds


def getCasesForICUByRequestedTime(impactInfections, severeImpactInfections):
  impactCasesForICU = math.trunc(0.05 * impactInfections)
  severeImpactCasesForICU = math.trunc(0.05 * severeImpactInfections)
  return impactCasesForICU,severeImpactCasesForICU

def getCasesForVentilatorsByRequestedTime(impactInfections, severeImpactInfections):
  impactCasesForVentilators = math.trunc(0.02 * impactInfections)
  severeImpactCasesForVentilators = math.trunc(0.02 * severeImpactInfections)
  return impactCasesForVentilators,severeImpactCasesForVentilators

def getDollarInflight(impactInfections, severeImpactInfections, totalDailyIncomeInUSD, timeToElapse):
  impactDollarinFlight = round(impactInfections * totalDailyIncomeInUSD * timeToElapse, 2)
  severeImpactDollarinFlight = round(severeImpactInfections * totalDailyIncomeInUSD * timeToElapse,2)
  return impactDollarinFlight, severeImpactDollarinFlight


def getData(impactCurrentlyInfected, impactInfections, impactSevereCases, impactHospitalBeds, impactCasesForICU, impactCasesForVentilators, impactDollarInFlight,severeImpactCurrentlyInfected, severeImpactInfections, severeImpactSevereCases, severeImpactHospitalBeds, severeImpactCasesForICU, severeImpactCasesForVentilators, severeImpactDollarInFlight, isSevere):
  
  return {
    "currentlyInfected" : severeImpactCurrentlyInfected if isSevere else impactCurrentlyInfected,
    "infectionsByRequestedTime" : severeImpactInfections if isSevere else impactInfections,
    "severeCasesByRequestedTime" : severeImpactSevereCases if isSevere else impactSevereCases,
    "hospitalBedsByRequestedTime" : severeImpactHospitalBeds if isSevere else impactHospitalBeds,
    "casesForICUByRequestedTime" : severeImpactCasesForICU if isSevere else impactCasesForICU,
    "casesForVentilatorsByRequestedTime" : severeImpactCasesForVentilators if isSevere else impactCasesForVentilators,
    "dollarsInFlight" : severeImpactDollarInFlight if isSevere else impactDollarInFlight
  }