import { Component, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
@Injectable({
  providedIn: 'root'
})
// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

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
  /*
    public checks: Array<any> = [
      { description: "Janvier", value: "1" },
      { description: "Février", value: "2" },
      { description: "Mars", value: "3" },
      { description: "Avril", value: "4" },
      { description: "Mai", value: "5" },
      { description: "Juin", value: "6" },
      { description: "Juillet", value: "7" },
      { description: "Août", value: "8" },
      { description: "Septembre", value: "9" },
      { description: "Octobre", value: "10" },
      { description: "Novembre", value: "11" },
      { description: "Décembre", value: "12" }
    ];*/

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

  renderedData: any;
  dataFrame: any;

  displayedColumns: string[] = ['CORSE', 'CIBLE', 'VENTE', 'CUMULE', 'BUDGET'];
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

  constructor(private DATACLEANING: ApiStat, private router: Router, fb: FormBuilder) {

    this.getCurrentMonth()
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource([]);

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
      this.cible.push(this.cible1)
      this.budget.push(this.budget1)
    }
    if (this.HiddenFev) {
      this.mois.push(2)
      this.cible.push(this.cible2)
      this.budget.push(this.budget2)
    }
    if (this.HiddenMar) {
      this.mois.push(3)
      this.cible.push(this.cible3)
      this.budget.push(this.budget3)
    }
    if (this.HiddenAvr) {
      this.mois.push(4)
      this.cible.push(this.cible4)
      this.budget.push(this.budget4)
    }
    if (this.HiddenMai) {
      this.mois.push(5)
      this.cible.push(this.cible5)
      this.budget.push(this.budget5)
    }
    if (this.HiddenJuin) {
      this.mois.push(6)
      this.cible.push(this.cible6)
      this.budget.push(this.budget6)
    }
    if (this.HiddenJuil) {
      this.mois.push(7)
      this.cible.push(this.cible7)
      this.budget.push(this.budget7)
    }
    if (this.HiddenAout) {
      this.mois.push(8)
      this.cible.push(this.cible8)
      this.budget.push(this.budget8)
    }
    if (this.HiddenSep) {
      this.mois.push(9)
      this.cible.push(this.cible9)
      this.budget.push(this.budget9)
    }
    if (this.HiddenOct) {
      this.mois.push(10)
      this.cible.push(this.cible10)
      this.budget.push(this.budget10)
    }
    if (this.HiddenNov) {
      this.mois.push(11)
      this.cible.push(this.cible11)
      this.budget.push(this.budget11)
    }
    if (this.HiddenDec) {
      this.mois.push(12)
      this.cible.push(this.cible12)
      this.budget.push(this.budget12)
    }

  }
  // function executed when user click on standardize button
  createFile = () => {
    console.log("test");
    console.log(this.annee)
    if (this.df1 != null && this.df2 != null) {
      if (this.annee == (new Date().getFullYear()).toString()) {
        this.getMois()
        console.log("test2")
        console.log(this.mois)
        console.log(this.cible)
        console.log(this.budget)
        this.value = 0
        this.DATACLEANING.sendFile(this.df1, this.df2, this.annee, this.mois, this.cible, this.budget).subscribe(
          data => {
            this.value = 10
            this.dataFrame = data;
            // to choose witch data gonna be showing in the table
            this.InitializeVisualization();
            // puts data into the datasource table
            this.dataSource = new MatTableDataSource(data);
            // execute the visualisation function
            this.executeVisualisation();
            // put Data into a rendered Data to export
            this.dataSource.connect().subscribe(d => this.renderedData = d);
            // add paginator to the data
            this.dataSource.paginator = this.paginator;
          },
          error => {
            console.log("error ", error);
          }
        );
      }
      if (this.annee == (new Date().getFullYear() + 1).toString()) {
        this.getMois()
        console.log("test2")
        console.log(this.mois)
        this.value = 0
        this.DATACLEANING.sendFilePlus(this.df1, this.df2, this.annee, this.mois).subscribe(
          data => {
            this.value = 10
            this.dataFrame = data;
            // to choose witch data gonna be showing in the table
            this.InitializeVisualization();
            // puts data into the datasource table
            this.dataSource = new MatTableDataSource(data);
            // execute the visualisation function
            this.executeVisualisation();
            // put Data into a rendered Data to export
            this.dataSource.connect().subscribe(d => this.renderedData = d);
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

  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
      { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
      { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    CORSE: new FormControl(true),
    CIBLE: new FormControl(true),
    VENTE: new FormControl(true),
    CUMUL: new FormControl(true),
    BUDGET: new FormControl(true)
  });

  // geting the checkBox
  CORSE = this.form.get('CORSE');
  CIBLE = this.form.get('CIBLE');
  VENTE = this.form.get('VENTE');
  CUMUL = this.form.get('CUMUL');
  BUDGET = this.form.get('BUDGET')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
    { def: 'CIBLE', label: 'CIBLE', show: this.CIBLE.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
    { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
}

