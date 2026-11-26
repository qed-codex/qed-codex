---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExceptionalDirichletZeroUniqueZeroFreeRegionStatement.lean",
  "declarations": [
    "GlobalTheory.T.exceptionalDirichletZero_unique_zeroFreeRegion"
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

## Uniqueness and separation of an exceptional Dirichlet zero

[Theorem ANT.1419](https://andrewodesky.com/rh/lean/GlobalTheory.T.exceptionalDirichletZero_unique_zeroFreeRegion/)

For a Dirichlet character $\chi$ modulo $M\ge3$, write $\chi^*$ for its associated primitive character. For $c_1>0$, call $(\chi,\beta)$ exceptional if $$\chi^2=1,\qquad 1-\frac{c_1}{\log M}<\beta<1,\qquad L(\beta,\chi^*)=0.$$ There is $c_0>0$ such that for every $0<c_1\le c_0$ there is $c>0$ with the following properties for every integer $M\ge3$. There is at most one exceptional pair modulo $M$. Every exceptional pair satisfies $$\chi\ne1,\quad \beta\ge\frac78,\quad L(\beta,\chi)=0,\quad \operatorname{ord}_{s=\beta}L(s,\chi)=1,\quad 1-\beta\ge\frac{c}{M^2\log M}.$$ For every character $\chi$ modulo $M$ and every zero $\rho$ of $L(s,\chi)$ with $\Re\rho<1$, either $\Im\rho=0$ and $(\chi,\Re\rho)$ is exceptional, or $$\Re\rho\le1-\frac{c}{\log(M(|\Im\rho|+2))}.$$
