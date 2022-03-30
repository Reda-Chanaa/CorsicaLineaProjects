import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcoCscComponent } from './conco-csc.component';

describe('ConcoCscComponent', () => {
  let component: ConcoCscComponent;
  let fixture: ComponentFixture<ConcoCscComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConcoCscComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConcoCscComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
