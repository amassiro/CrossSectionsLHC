import ROOT

from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText
from ROOT import gROOT
from ROOT import TGraph, TMultiGraph, TLegend, TH1F

import os.path

#x_values = [7.0, 8.0, 9.0, 10.0, 12.0, 13.0, 13.5, 14.0]
x_values = [7.0, 8.0, 9.0, 12.0, 13.0, 13.5, 14.0]

cc = TCanvas( 'cc', '', 800, 600 )

input_file = 'xsec_ecm.py'

samples = {}
if os.path.exists(input_file) :
  handle = open(input_file,'r')
  exec(handle)
  handle.close()


histo_ratio_14_13p6 = TH1F("histo_ratio_14_13p6", "", len(samples), 0, len(samples))
histo_ratio_14_13   = TH1F("histo_ratio_14_13",   "", len(samples), 0, len(samples))
histo_ratio_13p6_13 = TH1F("histo_ratio_13p6_13", "", len(samples), 0, len(samples))

mg = TMultiGraph()

leg = TLegend(0.2, 0.4, 0.3, 0.9);
leg.SetFillColor(0);

grs = []

iSample = 0

for key, value in samples.iteritems():
  gr = TGraph ()
  gr.SetTitle(key)
  # remove last element, that is the cross section
  #print value , " --> "
  value = value [:-1]
  #print value
  i = 0
  for scale in value:
    gr.SetPoint (i, x_values[i], scale) 
    #print i, x_values[i], scale
    i+=1

  gr.SetLineWidth(2)
  grs.append(gr)
  mg.Add (gr)
  leg.AddEntry(gr, key, "lp");
  
  print " " , key, " : 14/13.6 = " , gr.Eval(14) / gr.Eval(13.6)
  histo_ratio_14_13p6.Fill(iSample, gr.Eval(14) / gr.Eval(13.6))
  histo_ratio_14_13p6.SetBinError(iSample+1, 0)
  histo_ratio_14_13p6.GetXaxis().SetBinLabel(iSample+1, key)
  
  histo_ratio_14_13.Fill(iSample, gr.Eval(14.0) / gr.Eval(13.0))
  histo_ratio_14_13.SetBinError(iSample+1, 0)
  histo_ratio_14_13.GetXaxis().SetBinLabel(iSample+1, key)

  histo_ratio_13p6_13.Fill(iSample, gr.Eval(13.6) / gr.Eval(13.0))
  histo_ratio_13p6_13.SetBinError(iSample+1, 0)
  histo_ratio_13p6_13.GetXaxis().SetBinLabel(iSample+1, key)
  iSample+=1
  
  
mg.Draw("A pmc plc")
mg.GetXaxis().SetTitle("Energy [TeV]")
mg.GetYaxis().SetTitle("#sigma_{X} / #sigma_{7 TeV}")

leg.Draw();

cc.SaveAs("test.root")
cc.SaveAs("test.png")

  

histo_ratio_14_13p6.SetFillColor(ROOT.kBlue)
histo_ratio_14_13p6.SetLineColor(ROOT.kBlue)
histo_ratio_14_13p6.SetFillStyle(3002)
histo_ratio_14_13p6.GetYaxis().SetRangeUser(1.00, 1.50)
histo_ratio_14_13p6.GetYaxis().SetTitle("#sigma_{14} / #sigma_{13.6 TeV}")

#histo_ratio_14_13p6.Draw("hbar2")
histo_ratio_14_13p6.Draw("hbar")
cc.SaveAs("test_ratio_14_13p6.root")
cc.SaveAs("test_ratio_14_13p6.png")



histo_ratio_13p6_13.SetFillColor(ROOT.kRed)
histo_ratio_13p6_13.SetLineColor(ROOT.kRed)
histo_ratio_13p6_13.SetFillStyle(3002)
histo_ratio_13p6_13.GetYaxis().SetRangeUser(1.00, 1.50)
histo_ratio_13p6_13.GetYaxis().SetTitle("#sigma_{13.6} / #sigma_{13 TeV}")

histo_ratio_13p6_13.Draw("hbar")
cc.SaveAs("test_ratio_13p6_13.root")
cc.SaveAs("test_ratio_13p6_13.png")


histo_ratio_14_13.SetFillColor(ROOT.kGreen)
histo_ratio_14_13.SetLineColor(ROOT.kGreen)
histo_ratio_14_13.SetFillStyle(3001)
histo_ratio_14_13.GetYaxis().SetRangeUser(1.00, 1.50)
histo_ratio_14_13.GetYaxis().SetTitle("#sigma_{14} / #sigma_{13 TeV}")

histo_ratio_14_13.Draw("hbar")
cc.SaveAs("test_ratio_14_13.root")
cc.SaveAs("test_ratio_14_13.png")





histo_ratio_14_13.Draw("hbar")
histo_ratio_13p6_13.Draw("hbar same")

leg2 = TLegend(0.6, 0.4, 0.9, 0.9);
leg2.SetFillColor(0);
leg2.AddEntry(histo_ratio_14_13,   " 13 #rightarrow 14",   "lp");
leg2.AddEntry(histo_ratio_13p6_13, " 13 #rightarrow 13.6", "lp");
leg2.Draw();


histo_ratio_14_13.GetYaxis().SetTitle("#sigma_{X} / #sigma_{13 TeV}")

cc.SaveAs("test_ratio_14_13_and_13p6_13.root")
cc.SaveAs("test_ratio_14_13_and_13p6_13.png")



