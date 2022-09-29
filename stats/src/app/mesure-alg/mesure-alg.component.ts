import { Component, ElementRef, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { FormControl, FormGroup } from '@angular/forms';
import moment from 'moment';

@Injectable({
  providedIn: 'root'
})

// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }
  sendFile(File1: any, File2: any, ecart: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append('ecart', ecart);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/mesure-alg/', formData, { headers: header })
  }
  sendFilePlus(File1: any, File2: any, ecartSup: any, ecartInf: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append('ecartSup', ecartSup);
    formData.append('ecartInf', ecartInf);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/mesure-alg-plus/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  ID: string;
  NAVIRE: string;
  SENS: string;
  DATE: string;
  ECART: string;
  NIVEAU: string;
  VENTE: string;
  VENTEJ: string;
  ACTION: string;
}
@Component({
  selector: 'app-mesure-alg',
  templateUrl: './mesure-alg.component.html',
  styleUrls: ['./mesure-alg.component.css'],
  providers: [ApiStat]
})
export class MesureAlgComponent{

  day = new Date().getDate()
  mois = new Date().getMonth() + 1
  annees = new Date().getFullYear()

  date="MesureALG_" + this.day + "-" + this.mois + "-" + this.annees;

  dataFrame: any;
  @ViewChild('TABLE') table: ElementRef;
  displayedColumns: string[] = ['ID', 'NAVIRE', 'SENS', 'DATE', 'ECART', 'VENTE', 'VENTEJ','ACTION'];
  dataSource: MatTableDataSource<StatData>;

  ecartSup: string = null;
  ecartInf: string = null;
  annee: string;
  FecartSup = new FormControl('');
  FecartInf = new FormControl('');

  value:number=10
  df1: any = null;
  df2: any = null;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private DATACLEANING: ApiStat) {
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource([]);

  }
  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
  }
  // function executed when file is changed
  fileChangeListener2($event: any): void {
    this.df2 = $event.target.files[0]
  }

  changed1(value) {
    this.ecartSup = value.target.value
  }
  changed2(value) {
    this.ecartInf = value.target.value
  }

  deleteData() {
    this.dataSource = new MatTableDataSource([]);
  }

  printTable() {
    const printContents = document.getElementById("reporting").outerHTML
    var newWin = window.open("");  
    newWin.document.write(`
      <html>
        <head>
          <title>Mesure Vente ALG</title>
          <style>
          table th, table td {
            border-top: 0.5px solid #000;
            padding:0.5em;
          }
          </style>
        </head>
    <body onload="window.print();window.close()">${printContents}</body>
      </html>`
    );
    newWin.print();  
    newWin.close();
}
// function executed when user click on Reporting button
  createFile = () => {
    if (this.df1 != null && this.df2 != null) {
      if (this.ecartSup != null) {
        if (this.ecartInf == null) {
          this.value=0
          this.DATACLEANING.sendFile(this.df1, this.df2, this.ecartSup).subscribe(
            data => {
              this.value=10
              console.log(data)
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              data.forEach(element => {
                element.DATE=moment(element.DATE).format("DD/MM/YYYY HH:mm")
              });
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              this.dataSource.sort = this.sort;
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
        if (this.ecartInf != null) {
          this.value=0
          this.DATACLEANING.sendFilePlus(this.df1, this.df2, this.ecartSup, this.ecartInf).subscribe(
            data => {
              this.value=10
              console.log(data)
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              data.forEach(element => {
                element.DATE=moment(element.DATE).format("DD/MM/YYYY HH:mm")
              });
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              this.dataSource.sort = this.sort;
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
    let c0: Observable<boolean> = this.ID.valueChanges;
    let c1: Observable<boolean> = this.NAVIRE.valueChanges;
    let c2: Observable<boolean> = this.SENS.valueChanges;
    let c3: Observable<boolean> = this.DATE.valueChanges;
    let c4: Observable<boolean> = this.ECART.valueChanges;
    let c5: Observable<boolean> = this.VENTE.valueChanges;
    let c6: Observable<boolean> = this.VENTEJ.valueChanges;
    let c7: Observable<boolean> = this.ACTION.valueChanges;
    
    merge(c0, c1, c2, c3, c4, c5, c6).subscribe(v => {
      this.columnDefinitions[0].show = this.ID.value;
      this.columnDefinitions[1].show = this.NAVIRE.value;
      this.columnDefinitions[2].show = this.SENS.value;
      this.columnDefinitions[3].show = this.DATE.value;
      this.columnDefinitions[4].show = this.ECART.value;
      this.columnDefinitions[5].show = this.VENTE.value;
      this.columnDefinitions[6].show = this.VENTEJ.value;
      this.columnDefinitions[7].show = this.ACTION.value;
      
    });
  }
  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'ID', label: 'ID', show: this.ID.value },
      { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
      { def: 'SENS', label: 'SENS', show: this.SENS.value },
      { def: 'DATE', label: 'DATE', show: this.DATE.value },
      { def: 'ECART', label: 'ECART', show: this.ECART.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'VENTEJ', label: 'VENTEJ', show: this.VENTEJ.value },
      { def: 'ACTION', label: 'ACTION', show: this.ACTION.value },
      
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    ID: new FormControl(true),
    NAVIRE: new FormControl(true),
    SENS: new FormControl(true),
    DATE: new FormControl(true),
    ECART: new FormControl(true),
    VENTE: new FormControl(true),
    VENTEJ: new FormControl(true),
    ACTION: new FormControl(true),
    
  });

  // geting the checkBox
  ID = this.form.get('ID');
  NAVIRE = this.form.get('NAVIRE');
  SENS = this.form.get('SENS');
  DATE = this.form.get('DATE');
  ECART = this.form.get('ECART');
  VENTE = this.form.get('VENTE');
  VENTEJ = this.form.get('VENTEJ');
  ACTION = this.form.get('ACTION');
  

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'ID', label: 'ID', show: this.ID.value },
    { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
    { def: 'SENS', label: 'SENS', show: this.SENS.value },
    { def: 'DATE', label: 'DATE', show: this.DATE.value },
    { def: 'ECART', label: 'ECART', show: this.ECART.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'VENTEJ', label: 'VENTEJ', show: this.VENTEJ.value },
    { def: 'ACTION', label: 'ACTION', show: this.ACTION.value },
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }

}
