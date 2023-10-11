def has_special_char(s):
  for c in s:
    if not (c.isalpha() or c.isdigit() or c == ' '):
      return True
  return False


def checkName(name):
  if name.istitle() == False or name.isalpha() == False:
    return False
  return True


def checkPan(pan):
  first = pan[:5]
  second = pan[5:9]
  last = pan[9]
  if len(pan) != 10:
    return False
  elif first.isupper() == False or first.isalpha() == False:
    return False
  elif second.isdigit() == False:
    return False
  elif last.isupper() == False or last.isalpha() == False:
    return False
  elif " " in pan:
    return False
  elif has_special_char(pan) == True:
    return False
  else:
    return True


def checkDOB(dob):
  #dd/mm/yyyy
  if dob.count('/') >2:
    return False
  l = dob.split('/')
  day = int(l[0])
  year = int(l[2])
  month = int(l[1])
  if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or \
  month == 10 or month == 12:
    max_day_value = 31
  elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day_value = 30
  elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    max_day_value = 29
  else:
    max_day_value = 28

  if month < 1 or month > 12:
    return False
  elif day < 1 or day > max_day_value:
    return False
  else:
    return True


def checkDep(dep):
  departments = [
      "IT", 'Sales', 'Finance', "HR", "Management", 'Marketing', 'Accounting'
  ]
  if dep not in departments:
    return False
  return True


def checkAadhar(aad):
  if len(aad) != 12:
    return False
  elif aad[0] == 1 or aad[0] == 0:
    return False
  elif aad.isdigit() == False:
    return False
  else:
    return True


def checkAge(age):
  if age.isdigit() == False:
    return False
  elif int(age) < 20:
    return False
  else:
    return True


def checkSal(sal):
  if sal.isdigit() == False or int(sal) < 0:
    return False
  return True


def checkDesignation(des):
  designations = [
      'Trainee',
      'Software Developer',
      'Software Engineer',
      'Senior Software Developer',
      'Manager',
      'HR',
      'Tester',
      'Senior Manager',
      'CEO',
  ]
  if des not in designations:
    return False
  return True


def checkGender(gen):
  if gen not in ['Male', 'Female', 'Others']:
    return False
  return True


def checkState(st):
  states = [
      "Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh",
      "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
      "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
      "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
      "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
      "Uttar Pradesh", "Uttarakhand", "West Bengal",
      "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
      "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
      "Puducherry"
  ]
  if st not in states:
    return False
  return True


def checkCity(ct):
  cities = [
      'Abohar',
      'Agartala',
      'Agra',
      'Ahmadnagar',
      'Ahmedabad',
      'Ahmednagar',
      'Aizawl',
      'Ajmer',
      'Akola',
      'Aligarh',
      'Allahabad',
      'Allepy',
      'Ambala Cantt',
      'Amravati',
      'Amritsar',
      'Anand',
      'Anantapur',
      'Arrah',
      'Asansol',
      'Aurangabad',
      'Azamgarh',
      'Bahadurgarh',
      'Baharampur',
      'Balasore',
      'Balurghat',
      'Banda',
      'Bangalore',
      'Bangalore',
      'Bangalore',
      'Bankura',
      'Baramati',
      'Bareilly',
      'Barnala',
      'Barshi',
      'Baruipur',
      'Basirhat',
      'Basti',
      'Batala',
      'Bathinda',
      'Beawar',
      'Begusarai',
      'Belgaum',
      'Bellary',
      'Berhampur',
      'Bhagalpur',
      'Bharatpur',
      'Bhaurach',
      'Bhavnagar',
      'Bhind',
      'Bhiwani',
      'Bhopal',
      'Bhubaneswar',
      'Bid',
      'Bihar Shariff',
      'Bijapur',
      'Bijnor',
      'Bikaner',
      'Bilaspur',
      'Bogra',
      'Bokaro',
      'Bulandshahar',
      'Burdwan',
      'Calicut',
      'Chandigarh',
      'Chandrapur',
      'Chapra',
      'Chennai',
      'Chennai',
      'Chhindwara',
      'Chittagong',
      'Cochin',
      'Coimbatore',
      'Cooch Bihar',
      'Cuttack',
      'Daltonganj',
      'Davangere',
      'Dehradun',
      'Delhi',
      'Delhi',
      'Delhi',
      'Delhi',
      'Delhi',
      'Dhaka',
      'Dhaka',
      'Dhaka',
      'Dhanbad',
      'Dharmapuri',
      'Dibrugarh',
      'Dimapur',
      'Durg',
      'Durgapur',
      'Erode',
      'Faizabad',
      'Faridabad',
      'Faridkot',
      'Farrukhabad',
      'Firozabad',
      'Gandhinagar',
      'Gaya',
      'Ghaziabad',
      'Godhra',
      'Gondia',
      'Gopalganj',
      'Gulbarga',
      'Guna',
      'Guntur',
      'Gurgaon',
      'Guwahati',
      'Gwalior',
      'Habra',
      'Haldia',
      'Haldwani',
      'Hanumangarh',
      'Hardwar',
      'Hazaribagh',
      'Hissar',
      'Hoshiarpur',
      'Hospet',
      'Howrah',
      'Hubli',
      'Hyderabad',
      'Hyderabad',
      'Ichalkaranji',
      'Indore',
      'Itanagar',
      'Jabalpur',
      'Jaipur',
      'Jaisalmer',
      'Jalandhar',
      'Jalgaon',
      'Jalpaiguri',
      'Jammu',
      'Jamshedpur',
      'Jaunpur',
      'Jehanabad',
      'Jeypur',
      'Jhansi',
      'Jharsuguda',
      'Jhunjhunu',
      'Jind',
      'Jodhpur',
      'Jorhat',
      'Kaithal',
      'Kakinada',
      'Kannur',
      'Kanpur',
      'Karimnagar',
      'Karnal',
      'Kashipur',
      'Katihar',
      'Khammam',
      'Khandwa',
      'Khanna',
      'Khargone',
      'Khulna',
      'Kolhapur',
      'Kolkata',
      'Kolkata',
      'Kollam',
      'Korba',
      'Kota',
      'Kottayam',
      'Kullu',
      'Kurnool',
      'Kurukshetra',
      'Latur',
      'Lucknow',
      'Ludhiana',
      'Madurai',
      'Mahesana',
      'Mandalay',
      'Mandi',
      'Mandsaur',
      'Mangalore',
      'Mapusa',
      'Mathura',
      'Meerut',
      'Moga',
      'Mohali',
      'Moradabad',
      'Motihari',
      'Mughalsarai',
      'Muktsar',
      'Mumbai',
      'Mumbai',
      'Mumbai',
      'Mumbai-Kalyan',
      'Munger',
      'Muvattupuzha',
      'Muzaffarnagar',
      'Muzaffarpur',
      'Mysore',
      'Nagaon',
      'Nagercoil',
      'Nagpur',
      'Nalgonda',
      'Namakkal',
      'Nanded',
      'Nandyal',
      'Narnaul',
      'Nashik',
      'Nellore',
      'Mumbai',
      'Neyveli',
      'Nizamabad',
      'Noida',
      'Ongole',
      'Palakkad',
      'Panchkula',
      'Panipat',
      'Pathanamthitta',
      'Pathankot',
      'Patiala',
      'Patna',
      'Pollachi',
      'Pondicherry',
      'Pudukkottai',
      'Pune',
      'Purnea',
      'Purulia',
      'Rae Bareli',
      'Raichur',
      'Raipur',
      'Rajahmundry',
      'Rajshahi',
      'Rampur',
      'Ranchi',
      'Ratlam',
      'Raxaul Bazar',
      'Rewa',
      'Rewari',
      'Rohtak',
      'Roorkee',
      'Rourkela',
      'Rudrapur',
      'Rupnagar',
      'Sagar',
      'Saharanpur',
      'Saharsa',
      'Salem',
      'Samastipur',
      'Sambalpur',
      'Sangli',
      'Sasaram',
      'Satara',
      'Satna',
      'Serampore',
      'Shahjahanpur',
      'Shillong',
      'Shimla',
      'Shimoga',
      'Shivpuri',
      'Sikar',
      'Siliguri',
      'Sirsa',
      'Sitamarhi',
      'Sitapur',
      'Siwan',
      'Solan',
      'Solapur',
      'Sonipat',
      'Sri Ganganagar',
      'Srikakulam',
      'Sultanpur',
      'Surat',
      'Surendranagar',
      'Suri',
      'Tarn-Taran',
      'Tezpur',
      'Thanjavur',
      'Thrissur',
      'Tinsukia',
      'Tirunelveli',
      'Tirupati',
      'Tiruppur',
      'Tiruvannamalai',
      'Trichy',
      'Tumkur',
      'Tuticorin',
      'Udaipur',
      'Udaipur',
      'Udupi',
      'Ujjain',
      'Vadodara',
      'Valsad',
      'Vapi',
      'Varanasi',
      'Vidisha',
      'Vijayawada',
      'Visakhapatnam',
      'Warangal',
      'Yamunanagar',
      'Yavatmal',
  ]
  if ct not in cities:
    return False
  return True


def checkMobile(no):
  if no.isdigit() == False or len(no) != 10:
    return False
  return True


def checkType(type):
  if type not in ['Full-Time', 'Part-Time', 'Internship']:
    return False
  return True
