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

  sendFile(File1: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);

    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/stat-csc/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  ARMATEUR: string;
  NAVIRE: string;
  DATEHEUREDEPART: string;
  NAVIREW: string;
  DATEHEUREDEPARTW: string;
  MAXDATEFICHIER: string
}
@Component({
  selector: 'app-conco-csc',
  templateUrl: './conco-csc.component.html',
  styleUrls: ['./conco-csc.component.css'],
  providers: [ApiStat]
})
export class ConcoCscComponent {

  FAnnee1 = new FormControl('');
  FAnnee2 = new FormControl('')

  jourAFevN = new FormControl('');
  jourAFev = new FormControl('');
  moisAFevN = new FormControl('');
  moisAFev = new FormControl('');

  jourADecN = new FormControl('');
  jourADec = new FormControl('');
  moisADecN = new FormControl('');
  moisADec = new FormControl('');

  jourAOctN = new FormControl('');
  jourAOct = new FormControl('');
  moisAOctN = new FormControl('');
  moisAOct = new FormControl('');

  jourAAvrN = new FormControl('');
  jourAAvr = new FormControl('');
  moisAAvrN = new FormControl('');
  moisAAvr = new FormControl('');

  jourBFevN = new FormControl('');
  jourBFev = new FormControl('');
  moisBFevN = new FormControl('');
  moisBFev = new FormControl('');

  jourBDecN = new FormControl('');
  jourBDec = new FormControl('');
  moisBDecN = new FormControl('');
  moisBDec = new FormControl('');

  jourBOctN = new FormControl('');
  jourBOct = new FormControl('');
  moisBOctN = new FormControl('');
  moisBOct = new FormControl('');

  jourBAvrN = new FormControl('');
  jourBAvr = new FormControl('');
  moisBAvrN = new FormControl('');
  moisBAvr = new FormControl('');

  jourCFevN = new FormControl('');
  jourCFev = new FormControl('');
  moisCFevN = new FormControl('');
  moisCFev = new FormControl('');

  jourCDecN = new FormControl('');
  jourCDec = new FormControl('');
  moisCDecN = new FormControl('');
  moisCDec = new FormControl('');

  jourCOctN = new FormControl('');
  jourCOct = new FormControl('');
  moisCOctN = new FormControl('');
  moisCOct = new FormControl('');

  jourCAvrN = new FormControl('');
  jourCAvr = new FormControl('');
  moisCAvrN = new FormControl('');
  moisCAvr = new FormControl('');

  jourNAF: any;
  jourAF: any;
  moisNAF: any;
  moisAF: any;

  jourNAA: any;
  jourAA: any;
  moisNAA: any;
  moisAA: any;

  jourNAO: any;
  jourAO: any;
  moisNAO: any;
  moisAO: any;

  jourNAD: any;
  jourAD: any;
  moisNAD: any;
  moisAD: any;

  jourNBF: any;
  jourBF: any;
  moisNBF: any;
  moisBF: any;

  jourNBA: any;
  jourBA: any;
  moisNBA: any;
  moisBA: any;

  jourNBO: any;
  jourBO: any;
  moisNBO: any;
  moisBO: any;

  jourNBD: any;
  jourBD: any;
  moisNBD: any;
  moisBD: any;

  jourNCF: any;
  jourCF: any;
  moisNCF: any;
  moisCF: any;

  jourNCA: any;
  jourCA: any;
  moisNCA: any;
  moisCA: any;

  jourNCO: any;
  jourCO: any;
  moisNCO: any;
  moisCO: any;

  jourNCD: any;
  jourCD: any;
  moisNCD: any;
  moisCD: any;

  pickerPen1:Date;
  pickerPen2:Date;
  pickerPen3:Date;
  pickerPen4:Date;

  pickerPa1:Date;
  pickerPa2:Date;
  pickerPa3:Date;
  pickerPa4:Date;

  pickerAs1:Date;
  pickerAs2:Date;
  pickerAs3:Date;
  pickerAs4:Date;

  @ViewChild('TABLE') table: ElementRef;

  dataFrame: any;

  displayedColumns: string[] = ['ARMATEUR', 'NAVIRE', 'DATEHEUREDEPART', 'NAVIREW', 'DATEHEUREDEPARTW', 'MAXDATEFICHIER', 'INFO', 'RESEAU', 'PORTDEP', 'PORTARR', 'PORTDEPW', 'PORTARRW', 'MODELE', 'NUMPACKAGE', 'NUMPACKAGEW', 'MINDATEFICHIER'];
  dataSource: MatTableDataSource<StatData>;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  df1: any;
  annee: any;
  value: number;

  constructor(private DATACLEANING: ApiStat) {
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource([]);

  }

  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
  }


  deleteData() {
    this.dataSource = new MatTableDataSource([]);
  }
  // function executed when user click on Reporting button
  createFile = () => {

    if (this.df1 != null) {

      this.DATACLEANING.sendFile(this.df1).subscribe(
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
  //observable for the checkBox execute every time the checkBox is changed
  executeVisualisation() {
    let c0: Observable<boolean> = this.ARMATEUR.valueChanges;
    let c1: Observable<boolean> = this.NAVIRE.valueChanges;
    let c2: Observable<boolean> = this.DATEHEUREDEPART.valueChanges;
    let c3: Observable<boolean> = this.NAVIREW.valueChanges;
    let c4: Observable<boolean> = this.DATEHEUREDEPARTW.valueChanges;
    let c5: Observable<boolean> = this.MAXDATEFICHIER.valueChanges;
    let c6: Observable<boolean> = this.INFO.valueChanges;
    let c7: Observable<boolean> = this.RESEAU.valueChanges;
    let c8: Observable<boolean> = this.PORTDEP.valueChanges;
    let c9: Observable<boolean> = this.PORTARR.valueChanges;
    let c10: Observable<boolean> = this.PORTDEPW.valueChanges;
    let c11: Observable<boolean> = this.PORTARRW.valueChanges;
    let c12: Observable<boolean> = this.MODELE.valueChanges;
    let c13: Observable<boolean> = this.NUMPACKAGE.valueChanges;
    let c14: Observable<boolean> = this.NUMPACKAGEW.valueChanges;
    let c15: Observable<boolean> = this.MINDATEFICHIER.valueChanges;
    merge(c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15).subscribe(v => {
      this.columnDefinitions[0].show = this.ARMATEUR.value;
      this.columnDefinitions[1].show = this.NAVIRE.value;
      this.columnDefinitions[2].show = this.DATEHEUREDEPART.value;
      this.columnDefinitions[3].show = this.NAVIREW.value;
      this.columnDefinitions[4].show = this.DATEHEUREDEPARTW.value;
      this.columnDefinitions[5].show = this.MAXDATEFICHIER.value;
      this.columnDefinitions[6].show = this.INFO.value;
      this.columnDefinitions[7].show = this.RESEAU.value;
      this.columnDefinitions[8].show = this.PORTDEP.value;
      this.columnDefinitions[9].show = this.PORTARR.value;
      this.columnDefinitions[10].show = this.PORTDEPW.value;
      this.columnDefinitions[11].show = this.PORTARRW.value;
      this.columnDefinitions[12].show = this.MODELE.value;
      this.columnDefinitions[13].show = this.NUMPACKAGE.value;
      this.columnDefinitions[14].show = this.NUMPACKAGEW.value;
      this.columnDefinitions[15].show = this.MINDATEFICHIER.value;
    });
  }
  exportTable() {
    const ws: XLSX.WorkSheet = XLSX.utils.table_to_sheet(this.table.nativeElement);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'CSC');


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
      { def: 'ARMATEUR', label: 'ARMATEUR', show: this.ARMATEUR.value },
      { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
      { def: 'DATEHEUREDEPART', label: 'DATEHEUREDEPART', show: this.DATEHEUREDEPART.value },
      { def: 'NAVIREW', label: 'NAVIREW', show: this.NAVIREW.value },
      { def: 'DATEHEUREDEPARTW', label: 'DATEHEUREDEPARTW', show: this.DATEHEUREDEPARTW.value },
      { def: 'MAXDATEFICHIER', label: 'MAXDATEFICHIER', show: this.MAXDATEFICHIER.value },
      { def: 'INFO', label: 'INFO', show: this.INFO.value },
      { def: 'RESEAU', label: 'RESEAU', show: this.RESEAU.value },
      { def: 'PORTDEP', label: 'PORTDEP', show: this.PORTDEP.value },
      { def: 'PORTARR', label: 'PORTARR', show: this.PORTARR.value },
      { def: 'PORTDEPW', label: 'PORTDEPW', show: this.PORTDEPW.value },
      { def: 'PORTARRW', label: 'PORTARRW', show: this.PORTARRW.value },
      { def: 'MODELE', label: 'MODELE', show: this.MODELE.value },
      { def: 'NUMPACKAGE', label: 'NUMPACKAGE', show: this.NUMPACKAGE.value },
      { def: 'NUMPACKAGEW', label: 'NUMPACKAGEW', show: this.NUMPACKAGEW.value },
      { def: 'MINDATEFICHIER', label: 'MINDATEFICHIER', show: this.MINDATEFICHIER.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    ARMATEUR: new FormControl(true),
    NAVIRE: new FormControl(true),
    DATEHEUREDEPART: new FormControl(true),
    NAVIREW: new FormControl(true),
    DATEHEUREDEPARTW: new FormControl(true),
    MAXDATEFICHIER: new FormControl(true),
    INFO: new FormControl(true),
    RESEAU: new FormControl(true),
    PORTDEP: new FormControl(true),
    PORTARR: new FormControl(true),
    PORTDEPW: new FormControl(true),
    PORTARRW: new FormControl(true),
    MODELE: new FormControl(true),
    NUMPACKAGE: new FormControl(true),
    NUMPACKAGEW: new FormControl(true),
    MINDATEFICHIER: new FormControl(true)
  });

  // geting the checkBox
  ARMATEUR = this.form.get('ARMATEUR');
  NAVIRE = this.form.get('NAVIRE');
  DATEHEUREDEPART = this.form.get('DATEHEUREDEPART');
  NAVIREW = this.form.get('NAVIREW');
  DATEHEUREDEPARTW = this.form.get('DATEHEUREDEPARTW');
  MAXDATEFICHIER = this.form.get('MAXDATEFICHIER');
  INFO = this.form.get('INFO');
  RESEAU = this.form.get('RESEAU');
  PORTDEP = this.form.get('PORTDEP');
  PORTARR = this.form.get('PORTARR');
  PORTDEPW = this.form.get('PORTDEPW');
  PORTARRW = this.form.get('PORTARRW');
  MODELE = this.form.get('MODELE');
  NUMPACKAGE = this.form.get('NUMPACKAGE');
  NUMPACKAGEW = this.form.get('NUMPACKAGEW');
  MINDATEFICHIER = this.form.get('MINDATEFICHIER')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'ARMATEUR', label: 'ARMATEUR', show: this.ARMATEUR.value },
    { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
    { def: 'DATEHEUREDEPART', label: 'DATEHEUREDEPART', show: this.DATEHEUREDEPART.value },
    { def: 'NAVIREW', label: 'NAVIREW', show: this.NAVIREW.value },
    { def: 'DATEHEUREDEPARTW', label: 'DATEHEUREDEPARTW', show: this.DATEHEUREDEPARTW.value },
    { def: 'MAXDATEFICHIER', label: 'MAXDATEFICHIER', show: this.MAXDATEFICHIER.value },
    { def: 'INFO', label: 'INFO', show: this.INFO.value },
    { def: 'RESEAU', label: 'RESEAU', show: this.RESEAU.value },
    { def: 'PORTDEP', label: 'PORTDEP', show: this.PORTDEP.value },
    { def: 'PORTARR', label: 'PORTARR', show: this.PORTARR.value },
    { def: 'PORTDEPW', label: 'PORTDEPW', show: this.PORTDEPW.value },
    { def: 'PORTARRW', label: 'PORTARRW', show: this.PORTARRW.value },
    { def: 'MODELE', label: 'MODELE', show: this.MODELE.value },
    { def: 'NUMPACKAGE', label: 'NUMPACKAGE', show: this.NUMPACKAGE.value },
    { def: 'NUMPACKAGEW', label: 'NUMPACKAGEW', show: this.NUMPACKAGEW.value },
    { def: 'MINDATEFICHIER', label: 'MINDATEFICHIER', show: this.MINDATEFICHIER.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }

}
