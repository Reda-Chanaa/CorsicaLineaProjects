import { Component, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
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

  sendFile(File1: any, File2: any, annee: any, mois: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append("annee", annee);
    formData.append("mois", mois);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-alg/', formData, { headers: header })
  }
}
// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  ALGERIE: string;
  VENTEYES: string;
  VENTE: string;
  CUMUL: string;
  ECART: string;
}

@Component({
  selector: 'app-stat-alg',
  templateUrl: './stat-alg.component.html',
  styleUrls: ['./stat-alg.component.css'],
  providers: [ApiStat]
})
export class StatAlgComponent {
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

  displayedColumns: string[] = ['ALGERIE', 'VENTEYES', 'VENTE', 'CUMULE', 'ECART'];
  dataSource: MatTableDataSource<StatData>;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  element: any;
  df1: any;
  df2: any;
  annee: string;
  FAnnee = new FormControl('');
  mois: any = [];

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
    }
    if (this.HiddenFev) {
      this.mois.push(2)
    }
    if (this.HiddenMar) {
      this.mois.push(3)
    }
    if (this.HiddenAvr) {
      this.mois.push(4)
    }
    if (this.HiddenMai) {
      this.mois.push(5)
    }
    if (this.HiddenJuin) {
      this.mois.push(6)
    }
    if (this.HiddenJuil) {
      this.mois.push(7)
    }
    if (this.HiddenAout) {
      this.mois.push(8)
    }
    if (this.HiddenSep) {
      this.mois.push(9)
    }
    if (this.HiddenOct) {
      this.mois.push(10)
    }
    if (this.HiddenNov) {
      this.mois.push(11)
    }
    if (this.HiddenDec) {
      this.mois.push(12)
    }

  }
  changed(value) {
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
  // function executed when user click on reporting button
  createFile = () => {
    this.deleteData()
    this.mois = []
    console.log(this.annee)
    if (this.df1 != null && this.df2 != null) {
      if (this.annee == (new Date().getFullYear()).toString()) {
        this.getMois()
        console.log(this.mois)
        this.value = 0
        this.DATACLEANING.sendFile(this.df1, this.df2, this.annee, this.mois).subscribe(
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
    let c0: Observable<boolean> = this.ALGERIE.valueChanges;
    let c1: Observable<boolean> = this.VENTEYES.valueChanges;
    let c2: Observable<boolean> = this.VENTE.valueChanges;
    let c3: Observable<boolean> = this.CUMUL.valueChanges;
    let c4: Observable<boolean> = this.ECART.valueChanges;
    merge(c0, c1, c2, c3, c4).subscribe(v => {
      this.columnDefinitions[0].show = this.ALGERIE.value;
      this.columnDefinitions[1].show = this.VENTEYES.value;
      this.columnDefinitions[2].show = this.VENTE.value;
      this.columnDefinitions[3].show = this.CUMUL.value;
      this.columnDefinitions[4].show = this.ECART.value;
    });
  }

  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'ALGERIE', label: 'ALGERIE', show: this.ALGERIE.value },
      { def: 'VENTEYES', label: 'VENTEYES', show: this.VENTEYES.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
      { def: 'ECART', label: 'ECART', show: this.ECART.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    ALGERIE: new FormControl(true),
    VENTEYES: new FormControl(true),
    VENTE: new FormControl(true),
    CUMUL: new FormControl(true),
    ECART: new FormControl(true)
  });

  // geting the checkBox
  ALGERIE = this.form.get('ALGERIE');
  VENTEYES = this.form.get('VENTEYES');
  VENTE = this.form.get('VENTE');
  CUMUL = this.form.get('CUMUL');
  ECART = this.form.get('ECART')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'ALGERIE', label: 'ALGERIE', show: this.ALGERIE.value },
    { def: 'VENTEYES', label: 'VENTEYES', show: this.VENTEYES.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'CUMUL', label: 'CUMUL', show: this.CUMUL.value },
    { def: 'ECART', label: 'ECART', show: this.ECART.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
}
