## \file
 ## \ingroup tutorial_pyroot
 ## \notebook -js
 ## A Simple histogram drawing example
 ##
 ## \macro_image
## \macro_output
## \macro_code
##
## \author Wim Lavrijsen

from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText
from ROOT import gROOT
from ROOT import TGraph, TMultiGraph

import os.path

x_values = [7.0, 8.0, 9.0, 10.0, 12.0, 13.0, 13.5, 14.0]

cc = TCanvas( 'cc', '', 800, 600 )

input_file = 'xsec_ecm.py'

samples = {}
if os.path.exists(input_file) :
  handle = open(input_file,'r')
  exec(handle)
  handle.close()

mg = TMultiGraph()
  
grs = []

for key, value in samples.iteritems():
  gr = TGraph ()
  # remove last element, that is the cross section
  #print value , " --> "
  value = value [:-1]
  #print value
  i = 0
  for scale in value:
    gr.SetPoint (i, x_values[i], scale) 
    #print i, x_values[i], scale
    i+=1

  grs.append(gr)
  mg.Add (gr, key)

#print grs

mg.Draw("a")

cc.SaveAs("test.root")

  



