import { Component, ElementRef, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormControl, FormGroup } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { TableUtil } from "../tableUtil";
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
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-csc-info/', formData, { headers: header })
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
    return this.http.post(this.baseurl + '/stat-csc/', formData, { headers: header })
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
    return this.http.post(this.baseurl + '/stat-csc-plus/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  CORSE: string;
  CIBLE: string;
  VENTE: string;
  CUMUL: string;
  BUDGET: string;
}
@Component({
  selector: 'app-stat-csc',
  templateUrl: './stat-csc.component.html',
  styleUrls: ['./stat-csc.component.css'],
  providers: [ApiStat]
})
export class StatCscComponent {

  @ViewChild('TABLE') table: ElementRef;
  HiddenBudget = false
  HiddenCible = false

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

  displayedColumns: string[] = ['CORSE', 'CIBLE', 'VENTE', 'CUMULE', 'BUDGET', 'CUSTOM'];
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

  element: any;
  df1: any;
  df2: any;
  annee: string;
  FAnnee = new FormControl('');
  mois: any = [];
  cible: any = [];
  budget: any = [];

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
          }
          if (data[i].Mois == 2) {
            this.cible2 = data[i].Cible
            this.budget2 = data[i].Budget
          }
          if (data[i].Mois == 3) {
            this.cible3 = data[i].Cible
            this.budget3 = data[i].Budget
          }
          if (data[i].Mois == 4) {
            this.cible4 = data[i].Cible
            this.budget4 = data[i].Budget
          }
          if (data[i].Mois == 5) {
            this.cible5 = data[i].Cible
            this.budget5 = data[i].Budget
          }
          if (data[i].Mois == 6) {
            this.cible6 = data[i].Cible
            this.budget6 = data[i].Budget
          }
          if (data[i].Mois == 7) {
            this.cible7 = data[i].Cible
            this.budget7 = data[i].Budget
          }
          if (data[i].Mois == 8) {
            this.cible8 = data[i].Cible
            this.budget8 = data[i].Budget
          }
          if (data[i].Mois == 9) {
            this.cible9 = data[i].Cible
            this.budget9 = data[i].Budget
          }
          if (data[i].Mois == 10) {
            this.cible10 = data[i].Cible
            this.budget10 = data[i].Budget
          }
          if (data[i].Mois == 11) {
            this.cible11 = data[i].Cible
            this.budget11 = data[i].Budget
          }
          if (data[i].Mois == 12) {
            this.cible12 = data[i].Cible
            this.budget12 = data[i].Budget
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
    }

  }
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
  }
  saveChanges() {
    // puts data into the datasource table
    this.dataSource = new MatTableDataSource(this.dataFrame);
    console.log("frame ", this.dataFrame)
    console.log("source ", this.dataSource)
  }
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
    if (this.df1 != null && this.df2 != null) {
      if (this.annee == (new Date().getFullYear()).toString()) {
        this.getMois()
        if (this.HiddenCible && this.HiddenBudget) {
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
        if (this.HiddenCible && this.HiddenBudget) {
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
    let c0: Observable<boolean> = this.CORSE.valueChanges;
    let c1: Observable<boolean> = this.CIBLE.valueChanges;
    let c2: Observable<boolean> = this.VENTE.valueChanges;
    let c3: Observable<boolean> = this.CUMUL.valueChanges;
    let c4: Observable<boolean> = this.BUDGET.valueChanges;
    merge(c0, c1, c2, c3, c4).subscribe(v => {
      this.columnDefinitions[0].show = this.CORSE.value;
      this.columnDefinitions[1].show = this.CIBLE.value;
      this.columnDefinitions[2].show = this.VENTE.value;
      this.columnDefinitions[3].show = this.CUMUL.value;
      this.columnDefinitions[4].show = this.BUDGET.value;
    });
  }
  exportTable() {
    this.saveChanges()
    const ws: XLSX.WorkSheet = XLSX.utils.table_to_sheet(this.table.nativeElement);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');


    let day = new Date().getDate()
    let mois = new Date().getMonth() + 1
    let annee = new Date().getFullYear()
    let date = "ReportingCSC_" + this.annee + "_" + day + "-" + mois + "-" + annee + ".xlsx"
    console.log(date)
    /* save to file */
    XLSX.writeFile(wb, date.toString());
    //TableUtil.exportTableToExcel("reporting", date.toString());

  }
  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
      { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
      { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value },
      { def: 'CUSTOM', label: 'CUSTOM', show: this.CUSTOM.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    CORSE: new FormControl(true),
    CIBLE: new FormControl(true),
    VENTE: new FormControl(true),
    CUMUL: new FormControl(true),
    BUDGET: new FormControl(true),
    CUSTOM: new FormControl(false)
  });

  // geting the checkBox
  CORSE = this.form.get('CORSE');
  CIBLE = this.form.get('CIBLE');
  VENTE = this.form.get('VENTE');
  CUMUL = this.form.get('CUMUL');
  BUDGET = this.form.get('BUDGET');
  CUSTOM = this.form.get('CUSTOM')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
    { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
    { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value },
    { def: 'CUSTOM', label: 'CUSTOM', show: this.CUSTOM.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
}



