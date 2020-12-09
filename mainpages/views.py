from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from mainpages.forms import UserSelectionSignupForm
from mainpages.models import Employer, Applicant, JobPosting, JobCategory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from allauth.socialaccount.forms import SignupForm

import datetime
import json
import numpy as np

# Create your views here.

def azure_matchbox(request):
  import urllib

  userlookup = {"adam_e_carter": "2",	"alicia_r_coffey": "3",	"alyssa_j_belcher": "4",	"amanda_g_godfrey": "5",	"anne_t_dove": "6",	"annie_j_bernard": "7",	"annie_j_hays": "8",	"antonio_d_braithwaite": "9",	"arthur_s_simon": "10",	"bailey_m_alonzo": "11",	"barbara_c_post": "12",	"barbara_c_sousa": "13",	"barbara_m_chavez": "14",	"beatrice_r_downing": "15",	"bernice_c_knott": "16",	"beverly_d_dry": "17",	"bradley_g_chase": "18",	"brady_c_napier": "19",	"brandi_r_robinson": "20",	"brandon_a_oberlander": "21",	"brenda_j_burkhardt": "22",	"brenda_m_clark": "23",	"brian_h_stapp": "24",	"brian_m_johnson": "25",	"brook_j_whitworth": "26",	"carl_b_oconnor": "27",	"carl_s_rockwood": "28",	"carmen_r_arreola": "29",	"carol_j_morgan": "30",	"carol_m_dressler": "31",	"catherine_r_pinson": "32",	"cecily_p_skinner": "33",	"chad_s_flores": "34",	"chadwick_k_patten": "35",	"charles_m_byrnes": "36",	"charles_v_williams": "37",	"chris_l_beasley": "38",	"christie_s_grubbs": "39",	"christina_g_robinson": "40",	"christine_g_taylor": "41",	"clarence_i_fricke": "42",	"clifford_z_martinez": "43",	"clyde_c_palmer": "44",	"colleen_d_vasquez": "45",	"curtis_k_hodges": "46",	"dana_b_houston": "47",	"dana_b_narcisse": "48",	"david_c_mcmahan": "49",	"david_v_morgan": "50",	"dean_r_wright": "51",	"deeann_r_hoffman": "52",	"dianne_r_craft": "53",	"donald_r_roman": "54",	"dorothy_c_ashcraft": "55",	"dorothy_j_roger": "56",	"edward_j_rodriguez": "57",	"edward_v_espinal": "58",	"elaine_d_book": "59",	"elise_g_watkins": "60",	"elizabeth_m_petty": "61",	"erika_r_holloway": "62",	"fatimah_m_hart": "63",	"felicia_j_knutson": "64",	"frances_c_brown": "65",	"francine_a_mintz": "66",	"fred_m_murray": "67",	"gabriel_l_madison": "68",	"gail_d_fields": "69",	"gale_m_krom": "70",	"gary_j_glenn": "71",	"george_j_cook": "72",	"gregory_d_chapman": "73",	"gregory_m_williamson": "74",	"gwendolyn_j_amar": "75",	"harold_m_murdock": "76",	"henry_k_rowan": "77",	"ila_j_westgate": "78",	"inez_j_balling": "79",	"irene_j_hurst": "80",	"isaac_t_branan": "81",	"james_d_wetherbee": "82",	"james_f_sunderland": "83",	"james_j_crump": "84",	"james_m_bermudez": "85",	"james_n_james": "86",	"james_v_hartung": "87",	"james_w_ramirez": "88",	"jared_a_elliot": "89",	"jeffrey_c_hargrave": "90",	"jeffrey_l_marshall": "91",	"jeffrey_m_taylor": "92",	"jeffrey_m_whitehead": "93",	"jennifer_r_barclay": "94",	"jerry_c_elmer": "95",	"joanne_m_norton": "96",	"jodi_r_glaude": "97",	"john_d_peters": "98",	"john_j_hutchinson": "99",	"john_s_goods": "100",	"juanita_f_farias": "101",	"judith_j_archer": "102",	"julia_t_haliburton": "103",	"julio_m_chen": "104",	"karine_f_bello": "105",	"kathleen_b_barnes": "106",	"kelly_e_avendano": "107",	"kenneth_e_marshall": "108",	"kent_j_goldberg": "109",	"kimberly_j_harmon": "110",	"larry_l_moore": "111",	"laura_d_walton": "112",	"laura_t_gildersleeve": "113",	"leah_r_david": "114",	"leslie_d_bartels": "115",	"linda_c_job": "116",	"luis_e_erlandson": "117",	"lynda_r_kunz": "118",	"mandy_j_holland": "119",	"marc_j_farmer": "120",	"margaret_f_perry": "121",	"marion_c_baker": "122",	"marion_s_padgett": "123",	"martha_w_carter": "124",	"mary_a_trujillo": "125",	"mary_e_turner": "126",	"mason_c_wilson": "127",	"matthew_c_ketner": "128",	"matthew_n_pendleton": "129",	"michelle_d_walsh": "130",	"michelle_j_cornett": "131",	"mitsue_w_swafford": "132",	"monica_r_brown": "133",	"monique_t_schumann": "134",	"nancy_s_quinn": "135",	"nelson_v_leavitt": "136",	"ollie_j_vetter": "137",	"oscar_j_floyd": "138",	"oscar_j_ruiz": "139",	"pamela_j_reed": "140",	"patricia_l_longoria": "141",	"patricia_p_howard": "142",	"patricia_w_enoch": "143",	"patricia_w_rogers": "144",	"paul_n_henry": "145",	"paula_m_silva": "146",	"perry_k_manning": "147",	"peter_k_lewis": "148",	"preston_h_martins": "149",	"randall_k_hanley": "150",	"raymond_g_west": "151",	"richard_c_jacobson": "152",	"richard_e_larson": "153",	"robert_a_drees": "154",	"robert_b_wright": "155",	"robert_c_mullins": "156",	"robert_d_fernandez": "157",	"robert_r_parker": "158",	"robert_r_simon": "159",	"robert_s_moore": "160",	"robert_t_knox": "161",	"robert_v_hill": "162",	"roger_p_fabela": "163",	"ronald_b_weber": "164",	"ronald_d_morris": "165",	"rose_r_almanza": "166",	"sam_l_roach": "167",	"samuel_c_baker": "168",	"sandra_l_cady": "169",	"sarah_j_lee": "170",	"sarah_m_stallings": "171",	"sharon_j_apple": "172",	"sharon_s_hamm": "173",	"shawnta_e_rodriquez": "174",	"sherri_l_nguyen": "175",	"shirley_m_clark": "176",	"silvia_t_mcintosh": "177",	"sophie_j_white": "178",	"stanley_t_albrecht": "179",	"stephen_o_sweet": "180",	"stephen_p_snider": "181",	"steven_k_sanders": "182",	"susan_j_morman": "183",	"susan_w_hughes": "184",	"tarsha_r_hawks": "185",	"teresa_b_smith": "186",	"terry_a_tonkin": "187",	"thomas_a_thompson": "188",	"thomas_e_corley": "189",	"thomas_s_goforth": "190",	"tina_r_cruz": "191",	"tom_l_sullivan": "192",	"velma_s_terry": "193",	"victor_t_washburn": "194",	"virginia_k_taylor": "195",	"walter_b_burgos": "196",	"walter_e_carr": "197",	"walter_l_long": "198",	"walter_m_bishop": "199",	"wendy_r_jameson": "200",	"wilbur_m_clark": "201"}

  recommend = []
  
  if request.user != None and request.user.username in userlookup:

    data = {
      "Inputs": {
        "input1": {
          "ColumnNames": ["username", "id"],
          "Values": [[ 
            request.user.username, 
            userlookup[request.user.username], 
            ]]
        }
      }
    }
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/15d3874116954e749dcf8db99722f4a4/services/2c1610d5f6414354b06f110ea4b0921f/execute?api-version=2.0&details=true'
    api_key = 'JZgLrVt5KmFFYqVDq5x6THTxe/chMQiHvc0ZcKKB53Ss59cpjpl8dVa7gtqkugi9V6l9yjq1OLfrLHxYUQN5ZA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 
    req.method = "POST"

    response = urllib.request.urlopen(req)
    result = response.read()
    result = json.loads(result) # Convert JSON byte stream into dictionary
    prediction = result['Results']['output1']['value']['Values'][0]
    
    for p in prediction:
      if p != 'None' and p != request.user.username and p != None:
        recommend.append(p)
    
  return recommend

# View for about page template

def aboutPageView(request) :
  return render(request, 'applicationpages/about.html') 

import math

def calPageView(request) :
  
  calenderrender = []
    
    
  for job in JobPosting.objects.all():
    if job.appopendate.month == 12:
      day = job.appopendate.day
      calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Open Date'})
    if job.appclosingdate.month == 12:
      day = job.appclosingdate.day
      calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Closing Date'})
    if job.jobstartdate.month == 12:
      day = job.jobstartdate.day
      calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Open Date'})
    if job.decisiondate.month == 12:
      day = job.decisiondate.day
      calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Decision Date'})

  context = {
    'calenderobjects' : calenderrender
    }
  
  return render(request, 'applicationpages/jobcalender.html', context) 


def jpPageView(request) :
  
  jpq = JobPosting.objects.filter(ispublic=True)

  if request.GET.get("jobcat") != None and request.GET.get("jobcat") != '' :
    jpq = JobPosting.objects.none()
    jcList = JobCategory.objects.filter(name=request.GET.get("jobcat"))
    for jp in JobPosting.objects.filter(ispublic=True):
      for jc in jcList:
        if jc in jp.category.all():
          jpq = jpq.union(JobPosting.objects.filter(pk=jp.pk))
  
  context = {'postings' : jpq,
             'suggestions' : azure_matchbox(request), "cat": request.GET.get("jobcat")}
  
 
  return render(request, 'applicationpages/jobpostings.html', context)

# View for the index page

def indexPageView(request) :
    # sOutput = '<html><head><title>Main Page</title></head><body><p>This is the index page' + menu +'</body></html>'
    # return HttpResponse(sOutput) 
    if request.GET.get("jobcat") != None:
       return HttpResponseRedirect('/jobpostings/?jobcat='+request.GET.get("jobcat"))
    return render(request, 'homepage/index.html') 






