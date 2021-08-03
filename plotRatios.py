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


cc = TCanvas( 'cc', '', 800, 600 )

gr = TGraph ()




## Draw histogram hpx in first pad with the default option.
#pad1.cd()
#pad1.GetFrame().SetFillColor( 18 )
#hpx = gROOT.FindObject( 'hpx' )
#hpx.SetFillColor( 45 )
#hpx.DrawCopy()
#label1 = TPaveLabel( -3.5, 700, -1, 800, 'Default option' )
#label1.SetFillColor( 42 )
#label1.Draw()
##
## Draw hpx as a lego. Clicking on the lego area will show
## a "transparent cube" to guide you rotating the lego in real time.
#pad2.cd()
#hpx.DrawCopy( 'lego1' )
#label2 = TPaveLabel( -0.72, 0.74, -0.22, 0.88, 'option Lego1' )
#label2.SetFillColor( 42 )
#label2.Draw()
#label2a = TPaveLabel( -0.93, -1.08, 0.25, -0.92, 'Click on lego to rotate' )
#label2a.SetFillColor( 42 )
#label2a.Draw()
##
## Draw hpx with its errors and a marker.
#pad3.cd()
#pad3.SetGridx()
#pad3.SetGridy()
#pad3.GetFrame().SetFillColor( 18 )
#hpx.SetMarkerStyle( 21 )
#hpx.Draw( 'e1p' )
#label3 = TPaveLabel( 2, 600, 3.5, 650, 'option e1p' )
#label3.SetFillColor( 42 )
#label3.Draw()
##
## The following illustrates how to add comments using a PaveText.
## Attributes of text/lines/boxes added to a PaveText can be modified.
## The AddText function returns a pointer to the added object.
#pave = TPaveText( -3.78, 500, -1.2, 750 )
#pave.SetFillColor( 42 )
#t1 = pave.AddText( 'You can move' )
#t1.SetTextColor( 4 )
#t1.SetTextSize( 0.05 )
#pave.AddText( 'Title and Stats pads' )
#pave.AddText( 'X and Y axis' )
#pave.AddText( 'You can modify bin contents' )
#pave.Draw()
#c1.Update()



