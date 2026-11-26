---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use"
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

## A lower bound for the mean component volume slope, under arithmetic geometry hypotheses

[Theorem ARAK.1.1754](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use/)

Assume the following ten statements.

1. The full intersection-system existence hypothesis of ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)) holds.
2. ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)) hold.
3. The assertion of ([Arithmetic intersection and volume](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright/)) holds.
4. ([Projective resolution with normal-crossing coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement/)) holds.
5. Assertion 13 of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)) holds.
6. ([Hodge–Tate maps, orthogonality and a cokernel bound](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate/)) holds.
7. The assertion of ([Algebraization of holomorphic line bundle sections](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Gaga.gagaSections/)) holds.
8. ([An affine finite-flat quotient hypothesis for abelian schemes](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.GR.QuotientByFiniteFlatStatement/)) holds.
9. ([A polarized retract hypothesis over valuation rings](https://andrewodesky.com/rh/s/def-polarized-retract-valuation-ring.html)) holds.
10. ([A nef section-dimension asymptotic in homogeneous coordinates](https://andrewodesky.com/rh/s/def-nef-normalized-section-asymptotic.html)) holds.

Then there is a constant $C\ge0$ for which the following holds.

Let $D$ be an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$ and with the integers $k$ and $m$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), and suppose that $m^2\le k$. Let an enhanced geometric and adelic realization of $D$ satisfy the hypothesis “comparison laws for the enhanced realization” of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Let $j$ be an integer with $1\le j<m$, let $e\in\mathbb N$ and $o\in\mathbb R$, and let $\mathscr X$ be a level cover of the stage-$j$ moduli scheme of the realization that satisfies the good-cover hypothesis of the same page with parameters $e$ and $o$. Write $K$ for the coefficient field of $\mathscr X$, $(M_2,\mathfrak b_2,A_2)$ for its level, $(p,q)$ for its signature and $\Psi$ for its CM type, put $N=p+q$, and suppose that $\operatorname{lcm}(M_2,A_2)$ has at most $15$ distinct prime divisors.

Let $u=(u_{\tau i})_{\tau\in\Psi,\,0\le i<N}$ be an integral weight with $u_{\tau0}>u_{\tau1}>\cdots>u_{\tau,N-1}$ for every $\tau\in\Psi$, and let $g>0$ be a real number such that $$g\le|u_{\tau i}-u_{\tau i'}|\qquad\text{for all }\tau\in\Psi,\quad p\le i<N,\quad 0\le i'<N\text{ with }i'\ne i.$$ Put $$B=4|\Psi|N^2\left(1+\frac{\|u\|_\infty}{g}\right),$$ let $\mathcal Z$ be the set of irreducible components of the base change $\mathscr X_K$ of $\mathscr X$ to $K$, and for $Z\in\mathcal Z$ let $\operatorname{sl}_{Z,B}(u)$ be the volume slope of $Z$ at the weight $u$ and the cutoff $B$, as defined in ([Volume slopes of the components of a unitary moduli scheme](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.compVolSlope/)). Then there are real numbers $a_Z$, one for each $Z\in\mathcal Z$, such that $a_Z\le\operatorname{sl}_{Z,B}(u)$ for every $Z\in\mathcal Z$ and $$\frac1{|\mathcal Z|}\sum_{Z\in\mathcal Z}a_Z\ \ge\ -C\left(\left(\log B+\log\operatorname{rd}_E+\left|\operatorname{Re}\frac{L'(1,\chi_d)}{L(1,\chi_d)}\right|\right)\|u\|_1+q\sum_{\tau\in\Psi}\bigl(u_{\tau0}-u_{\tau,N-1}\bigr)\right).$$
