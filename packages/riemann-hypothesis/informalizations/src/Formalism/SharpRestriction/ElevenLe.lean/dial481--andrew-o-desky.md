---
{
  "module": "src/Formalism/SharpRestriction/ElevenLe.lean",
  "declarations": [
    "Formalism.MainNotions.SizesAt"
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

## Numerical size conditions for family members

[Definition / hypothesis PHT.D149](https://andrewodesky.com/rh/lean/Formalism.MainNotions.SizesAt/)

Hypothesis (numerical sizes). Use the arithmetic, scale and weight hypotheses of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). Set $$\theta=\varepsilon/100,\quad\varepsilon_0=\varepsilon/J,\quad\delta_1=x^{-\varepsilon/8},\quad N=k+m(t+1),\quad r_S=m/2-1,$$ $$N_*=2n\delta_1,\quad R_0=nx^{-\varepsilon},\quad Q=Q_Sqd,\quad \ell_A=\frac{kx^\varepsilon}{m\delta_2},\quad h_0=\eta/m,$$ $$\ell_*=\frac{mb}{nt^2(N+t)L^2+kn^2(S+t+L)}.$$ The ranks satisfy $$x^{2+8\varepsilon-\theta}\le n\le x^{2+8\varepsilon+\theta},\qquad x^{-\theta}\sqrt{x\delta_1}\le m\le x^\theta\sqrt{x\delta_1},$$ $$x^{9/2+10\varepsilon-\theta}\le k\le x^{9/2+10\varepsilon+\theta}.$$ Impose all the following rank comparisons: $$x^\theta m^5fLx^\varepsilon\le k,\quad8C_\Gamma m^5fL\le k,\quad k\le\sqrt{x}\,nR_0,\quad\sqrt{k/m}\le R_0,$$ $$m^2L\le k,\quad m\sqrt{x}\log x\le k,\quad x^\theta m^6L\le k\log k,\quad x^\theta m^3L\log\operatorname{rd}_E\le k(\log k)^2,$$ $$\log f\le\sqrt{r_S},\quad(\log f)^2\le m^2L,\quad x^\theta\log\log b\le rf\log r,\quad x^\theta L\le f\log k,\quad f\le m^2n,\quad f\le r^2.$$ Require also $$1\le t\le x^{C_t+\theta},\qquad Q^{36}t^{150}\le\sqrt b,$$ $$x^{\varepsilon_0/6}\le\log q,\quad x^{\varepsilon_0/5-\varepsilon_0/100}\le\log q\le x^{\varepsilon/5+\theta},\quad x^{\varepsilon_0/5-\varepsilon_0/100}\le\log d\le x^{\varepsilon/5+\theta}.$$ Furthermore, $$|\alpha|\le x^\varepsilon,\quad1\le\operatorname{rd}_E\le\frac{Q_S}{2}\sqrt{qd},\quad x^{-\theta}n\delta_1\le|T|\le N_*,$$ $$x^\varepsilon\le\mathcal G\le x^{\varepsilon+\theta},\quad\frac{4N_*x^\varepsilon\mathcal G+x^\theta\log x\,\mathcal G}{k}\le x^{-2},$$ $$b_v\le b'+N_*x^\varepsilon\mathcal G b'/k\ (v\in T),\quad x^{-\varepsilon}\le\delta_2,\quad L_w\le(\log x)^2.$$ All the following tolerance comparisons hold: $$t\le\eta\le\frac{b}{t^3fk^3},\quad\log\eta\le x^{\varepsilon/4},\quad t\eta\le w_0/x,\quad m(t+1)\eta\le w_0,$$ $$m(S+\eta)\le w_0L,\quad N\eta\le\delta_2mw_0,\quad\eta^2rL\le\delta_2mw_0^2,\quad r(b'+S)\log x\,\ell_A\le\delta_2mb.$$ Each of the following is at most $h_0$: $$12b/\ell_*+2t+8,\quad ktL,\quad x^\theta r^{19}f^5L,\quad4N^3+2t+6,$$ $$x^\theta km^{9/2},\quad2(r+mt)^3+t+3,\quad Nm^{10}.$$ Require $$b'+S+\eta+b/\ell_*<\ell_*,\qquad2\eta+t+8b/\ell_*+7<\ell_*,$$ $$Nm^{10}\le\Delta,\quad x^\theta mN\le\Delta,\quad\log\Delta\le x^{\varepsilon/4}/2,\quad kS\le w_0,\quad x^\theta mk\Delta\le w_0,$$ $$4S\le\mathcal G b'/k,\quad4x^\theta k^2\Delta\le\mathcal G b',\quad x^\theta m\log(\operatorname{rd}_E/2)\le k,\quad\sqrt b\le w_0.$$ For all indicated indices, $$B_{\tau,m-1}\le2B_{\tau,0},\qquad w_{j,\tau}\le X''w_{j',\tau'}\quad(1\le j,j'\le m).$$ For $i,i'\in\{0,1\}$ require $$(kb)^8\le g_i\le2g_{i'},\qquad\log g_i\le x^\theta L.$$ Finally, $$\log p_\Delta,\log p'_\Delta\le L,\qquad|\mathcal U|\le2^{k-3},\qquad s_0\ge11.$$ Here $\mathcal U$ is the source set, $s_0$ the splitting threshold, and $\alpha=\Re(L'/L)(1,\chi_d)$ as in ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). These numerical sizes are required only for members above the starting scale of ([Shared data in an arithmetic family](https://andrewodesky.com/rh/s/family-shared-data.html)); $x$ in each formula is the member's internal scale.
