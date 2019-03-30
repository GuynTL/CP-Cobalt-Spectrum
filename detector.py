

import numpy as np
import numpy.random as ran

import matplotlib.pyplot as plt

# from path import setParam, getParam

import time     # implementing dead time


# Have the dectector geometry 

Alrho = 2.7         # density of Al (g/cm3)
AlmacCS = 5.482e-02          # mass attenuation coeff for Al at 1.25 MeV for Compton scattering
AlmacPE =  1.688e-05         # mass attenuation coeff for Al at 1.25 Mev for photoelectric absorption
# NaIrho =
# NaImacCS =
# NaImacPE =
Al_thicc = 0.3      # mm, Al infront of the detector
det_r = 20          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction
sheild_thicc = 2    # mm, around the dectector
deadtime = 0.01     # s, optional? (non-trivial)
meandist = 1        # mm, mean distnce path travels in detector


##################################################################
#general functions which can be called easily

def comptonScatter(E):

    m_e = 0.5109989461   #MeV/c^2
    alpha = 1/137 #fine structure constant
    rc = 0.38616 #pm -> reduced Compton wavelength of an electron
    
    theta = np.arange(0,np.pi,0.01)   #range of possible theta angles (I beleive if we decrease 0.1 we will get a better resoultion)

    #probability for different scattering angles in Compton Effect is given by Klein-Nishina Forumula:

    P = 1/(1+(E/(m_e))*(1-np.cos(theta)))
    KN = (alpha**2)*(rc**2)*(P**2)* (P+ P**(-1) - (np.sin(theta)**2) )/2
    
    #return energy according to Compton Scatter Equation and randomly generated theta  

    totalSigma = sum(KN)  #total cross section(barns) - by integrating under Klein-Nishma Dist.
    randomTheta = np.random.choice(theta, 1,p=KN/totalSigma) 


    randomPhi = np.random.uniform(0,2*np.pi)   
    
    #plot

    plt.scatter(np.arange(0,np.pi,0.01), np.random.choice(theta, 315,p=KN/sum(KN)))
    #plt.plot(theta,KN)

    plt.show()

    Eprime = E/(1+(E/(m_e))*(1-np.cos(randomTheta))) #energy of scattered photon
    return [Eprime,randomPhi,randomTheta] #return energy according to Compton Scatter Equation and randomly generated theta






##################################################################



def attentuate(mac, rho):      # calculate a distance x travelled by a photon through some medium before an interaction
    num = ran.rand()
    x = np.log(num)/(-rho*mac)
    return x

def maxDistance(z, l):     # calculates the maximum allowed travel distance before exiting a volume. Should be compared to x from "attenuate" to determine if an interaction occrus
    d = z
    rho = np.sqrt((d*np.tan(r[1]* np.pi / 180))**2 + (d*np.tan(r[2]* np.pi / 180))**2)  # rho position of photon in cylindrical
    magr = np.sqrt(d**2 + rho**2)   # distance travelled from origin
    maxr = (magr/rho) * (det_r-rho)     # maximum allowed subsequent travel distance limited by radius of AL
    maxl = (magr/d) * l     # maximum allowed subsequent travel distance limited by length of Al
    maxx = min(maxr, maxl)
    return maxx

def setgeometry(lst):   # optional
    print ("")
    
def enterDect(r):    # there is a chance of the path deflecting off the Al shielding (r is vector in spherical)
    z = 25
    maxx = maxDistance(z, Al_thicc)
    print(maxx)
    x = attentuate(AlmacCS+AlmacPE, Alrho)
    if x < maxx:
        print('photon goes home')
        return False
    return True

def inDetector():   # photon is now in the scintillator

    print ("")
    return False

def energyLost():   # because of the deflection
    print ("")

def deflect():      # the path is deflected, set new path and energy lost
    print ("")
   
def distTrav(energy):     # distance the particle travels, take compton and photo effect into account, tempted to make another class for this
    print ("")
    return 0


