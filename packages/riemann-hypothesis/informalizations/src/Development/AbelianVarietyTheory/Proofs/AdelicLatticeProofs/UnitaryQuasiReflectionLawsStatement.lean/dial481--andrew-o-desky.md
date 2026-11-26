---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/UnitaryQuasiReflectionLawsStatement.lean",
  "declarations": [
    "GlobalTheory.T.unitaryQuasiReflection_laws"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Unitary quasireflections

[Theorem ALG.1113](https://andrewodesky.com/rh/lean/GlobalTheory.T.unitaryQuasiReflection_laws/)

Let $F,E$ be number fields with an $F$-algebra structure on $E$, and let $c\in\operatorname{Aut}_F(E)$ be a nonidentity involution. Let $G\in M_n(E)$ satisfy $c(G_{ab})=G_{ba}$ and $\det G\ne0$. Put $$h(v,w)=\sum_{a,b}v_aG_{ab}c(w_b).$$ For $x\in E^n$ with $h(x,x)\ne0$, define $$R_x(u)=I+\frac{u-1}{h(x,x)}x(Gc(x))^{\mathsf T}\qquad(u\in E).$$ Then $$R_x(u)v=v+\frac{(u-1)h(v,x)}{h(x,x)}x,\quad R_x(1)=I,\quad R_x(u)R_x(u')=R_x(uu').$$ If $u\,c(u)=1$, then $h(R_x(u)v,R_x(u)w)=h(v,w)$ for all $v,w$.
