import { Component, ElementRef, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormControl, FormGroup } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import * as XLSX from 'xlsx';
@Injectable({
  providedIn: 'root'
})
// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }

  getInf(annee: any): Observable<any> {

    let formData = new FormData();
    formData.append("annee", annee);
    console.log(formData);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-tun-info/', formData, { headers: header })
  }
  sendFile(File1: any, File2: any, annee: any, mois: any, cible: any, budget: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append("annee", annee);
    formData.append("mois", mois);
    formData.append("cible", cible);
    formData.append("budget", budget);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-tun/', formData, { headers: header })
  }
  sendFileObj(File1: any, File2: any, annee: any, mois: any, cible: any, budget: any, objectif: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append("annee", annee);
    formData.append("mois", mois);
    formData.append("cible", cible);
    formData.append("budget", budget);
    formData.append("objectif", objectif);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-tun-obj/', formData, { headers: header })
  }
  sendFilePlus(File1: any, File2: any, annee: any, mois: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append("annee", annee);
    formData.append("mois", mois);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-tun-plus/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  TUNISIE: string;
  CIBLE: string;
  VENTE: string;
  CUMUL: string;
  BUDGET: string;
  OBJECTIF: string
}
@Component({
  selector: 'app-stat-tun',
  templateUrl: './stat-tun.component.html',
  styleUrls: ['./stat-tun.component.css'],
  providers: [ApiStat]
})
export class StatTunClComponent {

  @ViewChild('TABLE') table: ElementRef;
  HiddenBudget = false
  HiddenCible = false
  HiddenObjectif = false

  HiddenJan = false
  HiddenFev = false
  HiddenMar = false
  HiddenAvr = false
  HiddenMai = false
  HiddenJuin = false
  HiddenJuil = false
  HiddenAout = false
  HiddenSep = false
  HiddenOct = false
  HiddenNov = false
  HiddenDec = false

  dataFrame: any;

  displayedColumns: string[] = ['TUNISIE', 'CIBLE', 'VENTE', 'CUMULE', 'BUDGET', 'OBJECTIF'];
  dataSource: MatTableDataSource<StatData>;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  janvier = new FormControl('');
  fevrier = new FormControl('');
  mars = new FormControl('');
  avril = new FormControl('');
  mai = new FormControl('');
  juin = new FormControl('');
  juillet = new FormControl('');
  aout = new FormControl('');
  septembre = new FormControl('');
  octobre = new FormControl('');
  novembre = new FormControl('');
  decembre = new FormControl('');

  Cjanvier = new FormControl('');
  Cfevrier = new FormControl('');
  Cmars = new FormControl('');
  Cavril = new FormControl('');
  Cmai = new FormControl('');
  Cjuin = new FormControl('');
  Cjuillet = new FormControl('');
  Caout = new FormControl('');
  Cseptembre = new FormControl('');
  Coctobre = new FormControl('');
  Cnovembre = new FormControl('');
  Cdecembre = new FormControl('');

  Ojanvier = new FormControl('');
  Ofevrier = new FormControl('');
  Omars = new FormControl('');
  Oavril = new FormControl('');
  Omai = new FormControl('');
  Ojuin = new FormControl('');
  Ojuillet = new FormControl('');
  Oaout = new FormControl('');
  Oseptembre = new FormControl('');
  Ooctobre = new FormControl('');
  Onovembre = new FormControl('');
  Odecembre = new FormControl('');

  cible1: any;
  cible2: any;
  cible3: any;
  cible4: any;
  cible5: any;
  cible6: any;
  cible7: any;
  cible8: any;
  cible9: any;
  cible10: any;
  cible11: any;
  cible12: any;

  budget1: any;
  budget2: any;
  budget3: any;
  budget4: any;
  budget5: any;
  budget6: any;
  budget7: any;
  budget8: any;
  budget9: any;
  budget10: any;
  budget11: any;
  budget12: any;

  Objectif1: any;
  Objectif2: any;
  Objectif3: any;
  Objectif4: any;
  Objectif5: any;
  Objectif6: any;
  Objectif7: any;
  Objectif8: any;
  Objectif9: any;
  Objectif10: any;
  Objectif11: any;
  Objectif12: any;

  element: any;
  df1: any;
  df2: any;
  annee: string;
  FAnnee = new FormControl('');
  mois: any = [];
  cible: any = [];
  budget: any = [];
  objectif: any = [];

  value: number;

  constructor(private DATACLEANING: ApiStat) {

    this.getCurrentMonth()
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource([]);
    this.getMois()
    this.getInfo()
  }
  getInfo() {
    this.DATACLEANING.getInf(this.annee).subscribe(
      data => {
        for (let i = 0; i < data.length; i++) {
          if (data[i].Mois == 1) {
            this.cible1 = data[i].Cible
            this.budget1 = data[i].Budget
            this.Objectif1 = data[i].Objectif
          }
          if (data[i].Mois == 2) {
            this.cible2 = data[i].Cible
            this.budget2 = data[i].Budget
            this.Objectif2 = data[i].Objectif
          }
          if (data[i].Mois == 3) {
            this.cible3 = data[i].Cible
            this.budget3 = data[i].Budget
            this.Objectif3 = data[i].Objectif
          }
          if (data[i].Mois == 4) {
            this.cible4 = data[i].Cible
            this.budget4 = data[i].Budget
            this.Objectif4 = data[i].Objectif
          }
          if (data[i].Mois == 5) {
            this.cible5 = data[i].Cible
            this.budget5 = data[i].Budget
            this.Objectif5 = data[i].Objectif
          }
          if (data[i].Mois == 6) {
            this.cible6 = data[i].Cible
            this.budget6 = data[i].Budget
            this.Objectif6 = data[i].Objectif
          }
          if (data[i].Mois == 7) {
            this.cible7 = data[i].Cible
            this.budget7 = data[i].Budget
            this.Objectif7 = data[i].Objectif
          }
          if (data[i].Mois == 8) {
            this.cible8 = data[i].Cible
            this.budget8 = data[i].Budget
            this.Objectif8 = data[i].Objectif
          }
          if (data[i].Mois == 9) {
            this.cible9 = data[i].Cible
            this.budget9 = data[i].Budget
            this.Objectif9 = data[i].Objectif
          }
          if (data[i].Mois == 10) {
            this.cible10 = data[i].Cible
            this.budget10 = data[i].Budget
            this.Objectif10 = data[i].Objectif
          }
          if (data[i].Mois == 11) {
            this.cible11 = data[i].Cible
            this.budget11 = data[i].Budget
            this.Objectif11 = data[i].Objectif
          }
          if (data[i].Mois == 12) {
            this.cible12 = data[i].Cible
            this.budget12 = data[i].Budget
            this.Objectif12 = data[i].Objectif
          }
        }
      },
      error => {
        console.log("error ", error);
      }
    );
  }

  getCurrentMonth() {
    let curdate = (new Date().getMonth() + 1).toString();
    this.annee = (new Date().getFullYear()).toString()
    if (curdate == "1") {
      this.HiddenJan = true
      this.HiddenFev = true
      this.HiddenMar = true
      this.HiddenAvr = true
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    else if (curdate == "2") {
      this.HiddenFev = true
      this.HiddenMar = true
      this.HiddenAvr = true
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "3") {
      this.HiddenMar = true
      this.HiddenAvr = true
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "4") {
      this.HiddenAvr = true
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "5") {
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "6") {
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "7") {
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "8") {
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "9") {
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "10") {
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "11") {
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (curdate == "12") {
      this.HiddenDec = true
    }
  }
  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
  }
  // function executed when file is changed
  fileChangeListener2($event: any): void {
    this.df2 = $event.target.files[0]
  }

  getMois() {
    if (this.HiddenJan) {
      this.mois.push(1)
      if (this.cible1 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible1)
      }
      if (this.budget1 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget1)
      }
      if (this.Objectif1 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif1)
      }
    }
    if (this.HiddenFev) {
      this.mois.push(2)
      if (this.cible2 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible2)
      }
      if (this.budget2 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget2)
      }
      if (this.Objectif2 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif2)
      }
    }
    if (this.HiddenMar) {
      this.mois.push(3)
      if (this.cible3 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible3)
      }
      if (this.budget3 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget3)
      }
      if (this.Objectif3 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif3)
      }
    }
    if (this.HiddenAvr) {
      this.mois.push(4)
      if (this.cible4 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible4)
      }
      if (this.budget4 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget4)
      }
      if (this.Objectif4 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif4)
      }
    }
    if (this.HiddenMai) {
      this.mois.push(5)
      if (this.cible5 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible5)
      }
      if (this.budget5 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget5)
      }
      if (this.Objectif5 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif5)
      }
    }
    if (this.HiddenJuin) {
      this.mois.push(6)
      if (this.cible6 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible6)
      }
      if (this.budget6 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget6)
      }
      if (this.Objectif6 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif6)
      }
    }
    if (this.HiddenJuil) {
      this.mois.push(7)
      if (this.cible7 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible7)
      }
      if (this.budget7 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget7)
      }
      if (this.Objectif7 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif7)
      }
    }
    if (this.HiddenAout) {
      this.mois.push(8)
      if (this.cible8 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible8)
      }
      if (this.budget8 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget8)
      }
      if (this.Objectif8 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif8)
      }
    }
    if (this.HiddenSep) {
      this.mois.push(9)
      if (this.cible9 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible9)
      }
      if (this.budget9 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget9)
      }
      if (this.Objectif9 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif9)
      }
    }
    if (this.HiddenOct) {
      this.mois.push(10)
      if (this.cible10 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible10)
      }
      if (this.budget10 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget10)
      }
      if (this.Objectif10 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif10)
      }
    }
    if (this.HiddenNov) {
      this.mois.push(11)
      if (this.cible11 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible11)
      }
      if (this.budget11 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget11)
      }
      if (this.Objectif11 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif11)
      }
    }
    if (this.HiddenDec) {
      this.mois.push(12)
      if (this.cible12 == null) {
        this.cible.push(0)
      }
      else {
        this.cible.push(this.cible12)
      }
      if (this.budget12 == null) {
        this.budget.push(0)
      }
      else {
        this.budget.push(this.budget12)
      }
      if (this.Objectif12 == null) {
        this.objectif.push(0)
      }
      else {
        this.objectif.push(this.Objectif12)
      }
    }

  }
  /*
  addColumn() {
    if (this.columnDefinitions[5].show == true) {
      this.columnDefinitions[5].show = false
      console.log("true ", this.columnDefinitions[5].show)
    }
    else {
      this.columnDefinitions[5].show = true
      console.log("false ", this.columnDefinitions[5].show)
    }
    console.log(this.getDisplayedColumns())
  }*/
  changed(value) {
    this.getInfo()
    if (value.target.value > (new Date().getFullYear()).toString()) {
      this.HiddenJan = true
      this.HiddenFev = true
      this.HiddenMar = true
      this.HiddenAvr = true
      this.HiddenMai = true
      this.HiddenJuin = true
      this.HiddenJuil = true
      this.HiddenAout = true
      this.HiddenSep = true
      this.HiddenOct = true
      this.HiddenNov = true
      this.HiddenDec = true
    }
    if (value.target.value == (new Date().getFullYear()).toString()) {
      this.HiddenJan = false
      this.HiddenFev = false
      this.HiddenMar = false
      this.HiddenAvr = false
      this.HiddenMai = false
      this.HiddenJuin = false
      this.HiddenJuil = false
      this.HiddenAout = false
      this.HiddenSep = false
      this.HiddenOct = false
      this.HiddenNov = false
      this.HiddenDec = false
      this.getCurrentMonth()
    }
  }

  deleteData() {
    this.dataSource = new MatTableDataSource([]);
  }
  // function executed when user click on Reporting button
  createFile = () => {
    this.mois = []
    this.budget = []
    this.cible = []
    this.objectif = []
    if (this.df1 != null && this.df2 != null) {
      if (this.annee == (new Date().getFullYear()).toString()) {
        this.getMois()
        if (this.HiddenCible && this.HiddenBudget && this.HiddenObjectif) {
          if (this.cible.length != 0) {
            if (this.budget.length != 0 && this.objectif.length) {
              this.DATACLEANING.sendFileObj(this.df1, this.df2, this.annee, this.mois, this.cible, this.budget, this.objectif).subscribe(
                data => {
                  this.dataFrame = data;
                  console.log(data)
                  // to choose witch data gonna be showing in the table
                  this.InitializeVisualization();
                  if (this.columnDefinitions[5].show == false) {
                    this.columnDefinitions[5].show = true
                  }
                  // puts data into the datasource table
                  this.dataSource = new MatTableDataSource(data);
                  // execute the visualisation function
                  this.executeVisualisation();
                  // add paginator to the data
                  this.dataSource.paginator = this.paginator;
                },
                error => {
                  console.log("error ", error);
                }
              );
            }
          }
        }
        else if (this.HiddenCible && this.HiddenBudget) {
          if (this.cible.length != 0) {
            if (this.budget.length != 0) {
              this.DATACLEANING.sendFile(this.df1, this.df2, this.annee, this.mois, this.cible, this.budget).subscribe(
                data => {
                  this.dataFrame = data;
                  // to choose witch data gonna be showing in the table
                  this.InitializeVisualization();
                  // puts data into the datasource table
                  this.dataSource = new MatTableDataSource(data);
                  // execute the visualisation function
                  this.executeVisualisation();
                  // add paginator to the data
                  this.dataSource.paginator = this.paginator;
                },
                error => {
                  console.log("error ", error);
                }
              );
            }
          }
        }
        else {
          this.DATACLEANING.sendFilePlus(this.df1, this.df2, this.annee, this.mois).subscribe(
            data => {
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              // execute the visualisation function
              this.executeVisualisation();
              // add paginator to the data
              this.dataSource.paginator = this.paginator;
            },
            error => {
              console.log("error ", error);
            }
          );
        }
      }
      if (this.annee == (new Date().getFullYear() + 1).toString()) {
        this.getMois()
        console.log(this.objectif)
        if (this.HiddenCible && this.HiddenBudget && this.HiddenObjectif) {
          if (this.cible.length != 0) {
            if (this.budget.length != 0 && this.objectif.length) {
              this.DATACLEANING.sendFileObj(this.df1, this.df2, this.annee, this.mois, this.cible, this.budget, this.objectif).subscribe(
                data => {
                  this.dataFrame = data;
                  console.log(data)
                  // to choose witch data gonna be showing in the table
                  this.InitializeVisualization();
                  if (this.columnDefinitions[5].show == false) {
                    this.columnDefinitions[5].show = true
                  }
                  // puts data into the datasource table
                  this.dataSource = new MatTableDataSource(data);
                  // execute the visualisation function
                  this.executeVisualisation();
                  // add paginator to the data
                  this.dataSource.paginator = this.paginator;
                },
                error => {
                  console.log("error ", error);
                }
              );
            }
          }
        }
        else if (this.HiddenCible && this.HiddenBudget) {
          if (this.cible.length != 0) {
            if (this.budget.length != 0) {
              this.DATACLEANING.sendFile(this.df1, this.df2, this.annee, this.mois, this.cible, this.budget).subscribe(
                data => {
                  this.dataFrame = data;
                  // to choose witch data gonna be showing in the table
                  this.InitializeVisualization();
                  // puts data into the datasource table
                  this.dataSource = new MatTableDataSource(data);
                  // execute the visualisation function
                  this.executeVisualisation();
                  // add paginator to the data
                  this.dataSource.paginator = this.paginator;
                },
                error => {
                  console.log("error ", error);
                }
              );
            }
          }
        }
        else {
          this.DATACLEANING.sendFilePlus(this.df1, this.df2, this.annee, this.mois).subscribe(
            data => {
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              // execute the visualisation function
              this.executeVisualisation();
              // add paginator to the data
              this.dataSource.paginator = this.paginator;
            },
            error => {
              console.log("error ", error);
            }
          );
        }
      }
    }
  }

  //observable for the checkBox execute every time the checkBox is changed
  executeVisualisation() {
    let c0: Observable<boolean> = this.TUNISIE.valueChanges;
    let c1: Observable<boolean> = this.CIBLE.valueChanges;
    let c2: Observable<boolean> = this.VENTE.valueChanges;
    let c3: Observable<boolean> = this.CUMUL.valueChanges;
    let c4: Observable<boolean> = this.BUDGET.valueChanges;
    let c5: Observable<boolean> = this.OBJECTIF.valueChanges;
    merge(c0, c1, c2, c3, c4, c5).subscribe(v => {
      this.columnDefinitions[0].show = this.TUNISIE.value;
      this.columnDefinitions[1].show = this.CIBLE.value;
      this.columnDefinitions[2].show = this.VENTE.value;
      this.columnDefinitions[3].show = this.CUMUL.value;
      this.columnDefinitions[4].show = this.BUDGET.value;
      this.columnDefinitions[5].show = this.OBJECTIF.value;
    });
  }
  exportTable() {
    const ws: XLSX.WorkSheet = XLSX.utils.table_to_sheet(this.table.nativeElement);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'TUN');


    let day = new Date().getDate()
    let mois = new Date().getMonth() + 1
    let annee = new Date().getFullYear()
    let date = "ReportingTUN_" + this.annee + "_" + day + "-" + mois + "-" + annee + ".xlsx"
    console.log(date)
    /* save to file */
    XLSX.writeFile(wb, date.toString());
    //TableUtil.exportTableToExcel("reporting", date.toString());

  }
  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'TUNISIE', label: 'TUNISIE', show: this.TUNISIE.value },
      { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
      { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value },
      { def: 'OBJECTIF', label: 'OBJECTIF', show: this.OBJECTIF.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    TUNISIE: new FormControl(true),
    CIBLE: new FormControl(true),
    VENTE: new FormControl(true),
    CUMUL: new FormControl(true),
    BUDGET: new FormControl(true),
    OBJECTIF: new FormControl(false)
  });

  // geting the checkBox
  TUNISIE = this.form.get('TUNISIE');
  CIBLE = this.form.get('CIBLE');
  VENTE = this.form.get('VENTE');
  CUMUL = this.form.get('CUMUL');
  BUDGET = this.form.get('BUDGET');
  OBJECTIF = this.form.get('OBJECTIF')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'TUNISIE', label: 'TUNISIE', show: this.TUNISIE.value },
    { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
    { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value },
    { def: 'OBJECTIF', label: 'OBJECTIF', show: this.OBJECTIF.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
}