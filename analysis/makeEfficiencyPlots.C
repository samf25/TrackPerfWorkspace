// Include the necessary ROOT headers
#include <TFile.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TEfficiency.h>
#include <TLegend.h>
#include <TStyle.h>

// Function to count non-empty bins
double dataCount(TH1* hist) {
	double count = 0;
	for (int i = 1; i <= hist->GetNbinsX(); ++i) 
		count += hist->GetBinContent(i);
	return count;
}


void makeEfficiencyPlots() {
	// Open File
	TFile* f = TFile::Open("/isilon/export/home/sferrar2/TrackPerfWorkspace/example/histograms.root");
	if (!f) {
		std::cerr << "Error: Cannot open file." << std::endl;
		return;
	}
	
	// Find Graphs in Directories
	TDirectory* reals = (TDirectory*)f->Get("real");
	TDirectory* fakes = (TDirectory*)f->Get("fake");
	
	TH1F* rPassedEta = (TH1F*)reals->Get("eff_fake_eta_passed");
	TH1F* rTotalEta = (TH1F*)reals->Get("eff_fake_eta_total");
	TH1F* fPassedEta = (TH1F*)fakes->Get("eff_fake_eta_passed");
	TH1F* fTotalEta = (TH1F*)fakes->Get("eff_fake_eta_total");
	
	TH1F* rPassedpT = (TH1F*)reals->Get("eff_fake_pt_passed");
        TH1F* rTotalpT = (TH1F*)reals->Get("eff_fake_pt_total");
        TH1F* fPassedpT = (TH1F*)fakes->Get("eff_fake_pt_passed");
        TH1F* fTotalpT = (TH1F*)fakes->Get("eff_fake_pt_total");
	
	// Ensure we found everything
	if (!reals || !fakes || 
	    !rPassedEta || !rTotalEta || !fPassedEta || !fTotalEta || 
	    !rPassedpT || !rTotalpT || !fPassedpT || !fTotalpT ) {
		std::cerr << "Error: Cannot retrieve a histogram or directory." << std::endl;
		return;
	}
	
	// Make Canvases
	TCanvas* can1 = new TCanvas("c1", "Reconstruction Efficiency vs Eta", 800, 600);
	TCanvas* can2 = new TCanvas("c2", "Reconstruction Efficiency vs pT", 800, 600);
	TCanvas* can3 = new TCanvas("c3", "Fake Rate vs Eta", 800, 600);
	TCanvas* can4 = new TCanvas("c4", "Fake Rate vs pT", 800, 600);

	// Set Padding for y-axis Labal
	float pad = 0.15;
	can1->SetLeftMargin(pad);
        can2->SetLeftMargin(pad);
        can3->SetLeftMargin(pad);
        can4->SetLeftMargin(pad);
		
	// Make TEfficiency Plots
	TEfficiency* rEta = new TEfficiency(*rPassedEta, *rTotalEta);
	TEfficiency* rpT = new TEfficiency(*rPassedpT, *rTotalpT);
	TEfficiency* fEta = new TEfficiency(*fPassedEta, *fTotalEta);
        TEfficiency* fpT = new TEfficiency(*fPassedpT, *fTotalpT);
	
	// Set Titles and axes
	rEta->SetTitle("Reconstruction Efficiency vs. Eta;Truth Eta;Efficiency");
	rpT->SetTitle("Reconstruction Efficiency vs. pT;Truth pT;Efficiency");
	fEta->SetTitle("Fake Rate vs. Eta;Reconstructed Eta;Fake Rate");
        fpT->SetTitle("Fake Rate vs. pT;Reconstructed pT;Fake Rate");

	// Set Visuals
	rEta->SetMarkerStyle(20);
	rEta->SetMarkerSize(0.5);
        rpT->SetMarkerStyle(20);
        rEta->SetMarkerSize(0.5);
        fEta->SetMarkerStyle(20);
        fEta->SetMarkerSize(0.5);
        fpT->SetMarkerStyle(20);
        fpT->SetMarkerSize(0.5);

	// Create legends
	float x1 = 0.8;
	float x2 = 0.98;
	float y1 = 0.88;
	float y2 = 0.94;
	TLegend* leg1 = new TLegend(x1, y1, x2, y2);
	TLegend* leg2 = new TLegend(x1, y1, x2, y2);
	TLegend* leg3 = new TLegend(x1, y1, x2, y2);
	TLegend* leg4 = new TLegend(x1, y1, x2, y2);

	// Set font size for legends
	float font = 0.03;
	leg1->SetTextSize(font);
	leg2->SetTextSize(font);
	leg3->SetTextSize(font);
	leg4->SetTextSize(font);	
	
	// Margins for legends
	float marg = 0.05;
	leg1->SetMargin(marg);
	leg2->SetMargin(marg);
	leg3->SetMargin(marg);
	leg4->SetMargin(marg);

	// Fill legends
	leg1->AddEntry(rEta, Form("Entries %*d", 10, (int)dataCount(rPassedEta)), "");
	leg2->AddEntry(rpT, Form("Entries %*d", 10, (int)dataCount(rPassedpT)), "");
	leg3->AddEntry(fEta, Form("Entries %*d", 10, (int)dataCount(fPassedEta)), "");
	leg4->AddEntry(fpT, Form("Entries %*d", 10, (int)dataCount(fPassedpT)), "");

	// Draw graphs
	can1->cd();
	rEta->Draw();
	leg1->Draw();
	can2->cd();
        rpT->Draw();
	leg2->Draw();
	can3->cd();
        fEta->Draw();
	leg3->Draw();
	can4->cd();
	fpT->Draw();
	leg4->Draw();
	
	// Save Canvases
	can1->SaveAs("efficiency_eta.png");
	can2->SaveAs("efficiency_pT.png");
	can3->SaveAs("fakerate_eta.png");
	can4->SaveAs("fakerate_pT.png");
	
	// Close File
	f->Close();
}
