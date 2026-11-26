---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/LinksLemmas.lean",
  "declarations": [
    "Formalism.IndefR.Links.HostHyp"
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

## Weight gaps for analytic comparisons

[Definition / hypothesis ARAK.D234](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.HostHyp/)

Hypothesis (weight gaps for analytic comparisons). Use the ranks, words and weight arrays of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) and ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)). Write $U_{\tau,i},V_{\tau,i},B_{\tau,j},E_{\tau,j}$ for the arrays of the distinguished word and $B_{u,\tau,j}$ for those of any word $u$. The indices of $U,V,B,E$ have lengths $k,k-1,m,m$, respectively. At every selected embedding, impose the interlacing and basic gap conditions of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)).

Set $r=k+m-1$, $N_m=k+m(t+1)$, and define, for every natural $a$, $$\lambda_\tau(a)=\begin{cases}V_{\tau,a},&a<k-1,\\-B_{\tau,a-(k-1)},&k-1\le a<k-1+m,\\0,&\text{otherwise}.\end{cases}$$ Require $$\lambda_\tau(a)-\lambda_\tau(a+1)\ge100r^4\quad(a+1<r),\qquad \lambda_\tau(k-2)-\lambda_\tau(k-1)\ge100r^4.$$ For every word $u$, every $\tau$, and every $j+1<m$, require both $$B_{u,\tau,j+1}-B_{u,\tau,j}\ge4N_m^3+2t+6,\qquad B_{u,\tau,j+1}-B_{u,\tau,j}\ge256r^4.$$

For every $0\le i<m$, choose a weight at stage $i+1$ in the sense of ([Cuspidal sections and their integral Fourier data](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)). These weights are additional choices; no equation identifies them with the displayed $U,V,B,E$ arrays.
