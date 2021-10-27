# A "Responsive" Web Application for Standardizing, Verifying and Validating Transport Data

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 1.0.0 and angular 4.x.

## Code scaffolding

Run in FrontEnd Folder `ng generate component component-name` to generate a new component or `ng g c component-name`. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run in FrontEnd Folder `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run in FrontEnd Folder `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run in FrontEnd Folder `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.


## Terminal Commands

1. Install NodeJs from [NodeJs Official Page](https://nodejs.org/en).
2. Open Terminal
3. Go to your file project
4. Make sure you have installed [Angular CLI](https://github.com/angular/angular-cli) already. If not, please install by running in terminal: ```npm install -g @angular/cli```.
5. Run in FrontEnd terminal: ```npm install```.
6. For windows, Run in terminal of the BackEnd Folder : ``` py -m pip install --user virtualenv``` for installing a virtual envirenement, then ```py -m venv venv``` to create a venv folder then run ```./venv/scripts/activate``` to activate it,
7. For Mac, Run in terminal of the BackEnd Folder : ``` python3 -m pip install --user``` for installing a virtual envirenement, then ```python3 -m venv venv``` to create a venv folder then run ``` source venv/bin/activate``` to activate virtual envirenement.
8. Run ```pip install -r requirements.txt``` to install all the modules that you gonna need on your Mac.
9. Run ```pip install -r requirements_win.txt``` to install all the modules that you gonna need on your windows.
10. When its Ok, Run ```python manage.py runserver``` to run the server of the BackEnd.
11. Back to the FrontEnd, Run `ng serve --open` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

12. if you add a package in backend, please run ```pip freeze > requirements.txt``` to add automatically the module name and his version (You can check the file in BackEnd folder). 

### What's included

Within the download you'll find the following directories and files:

```
Now Ui Dashboard
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── angular-cli.json
├── documentation
├── e2e
├── karma.conf.js
├── package.json
├── protractor.conf.js
├── src
│   ├── app
│   │   ├── app.component.css
│   │   ├── app.component.html
│   │   ├── app.component.spec.ts
│   │   ├── app.component.ts
│   │   ├── app.module.ts
│   │   ├── app.routing.ts
│   │   ├── components
│   │   │   ├── components.module.ts
│   │   │   ├── footer
│   │   │   │   ├── footer.component.css
│   │   │   │   ├── footer.component.html
│   │   │   │   ├── footer.component.spec.ts
│   │   │   │   └── footer.component.ts
│   │   │   ├── navbar
│   │   │   │   ├── navbar.component.css
│   │   │   │   ├── navbar.component.html
│   │   │   │   ├── navbar.component.spec.ts
│   │   │   │   └── navbar.component.ts
│   │   │   └── sidebar
│   │   │       ├── sidebar.component.css
│   │   │       ├── sidebar.component.html
│   │   │       ├── sidebar.component.spec.ts
│   │   │       └── sidebar.component.ts
│   │   ├── dashboard
│   │   │   ├── dashboard.component.css
│   │   │   ├── dashboard.component.html
│   │   │   ├── dashboard.component.spec.ts
│   │   │   └── dashboard.component.ts
│   │   ├── layouts
│   │   │   └── admin-layout
│   │   │       ├── admin-layout.component.html
│   │   │       ├── admin-layout.component.scss
│   │   │       ├── admin-layout.component.spec.ts
│   │   │       ├── admin-layout.component.ts
│   │   │       ├── admin-layout.module.ts
│   │   │       └── admin-layout.routing.ts
│   │   ├── table-list
│   │   │   ├── table-list.component.css
│   │   │   ├── table-list.component.html
│   │   │   ├── table-list.component.spec.ts
│   │   │   └── table-list.component.ts
│   │   ├── typography
│   │   │   ├── typography.component.css
│   │   │   ├── typography.component.html
│   │   │   ├── typography.component.spec.ts
│   │   │   └── typography.component.ts
│   ├── assets
│   │   ├── demo
│   │   ├── fonts
│   │   ├── img
│   │   └── scss
│   │       ├── now-ui-dashboard
│   │       └── now-ui-dashboard.scss
│   ├── environments
│   ├── favicon.ico
│   ├── index.html
│   ├── main.ts
│   ├── polyfills.ts
│   ├── styles.css
│   ├── test.ts
│   ├── tsconfig.app.json
│   ├── tsconfig.spec.json
│   └── typings.d.ts
├── tsconfig.json
├── tslint.json
└── typings
```
