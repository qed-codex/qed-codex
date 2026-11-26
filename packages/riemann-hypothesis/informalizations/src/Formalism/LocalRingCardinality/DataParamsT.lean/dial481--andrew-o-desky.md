---
{
  "module": "src/Formalism/LocalRingCardinality/DataParamsT.lean",
  "declarations": [
    "Formalism.BasicNotions.ParamsT"
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

## Theta parameters and precision inequalities

[Definition / hypothesis PHT.D150](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ParamsT/)

Hypothesis (theta parameters). Use the arithmetic, scale and weight hypotheses of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). Put $N=k+m(t+1)$, $h_0=\eta/m$, $\delta_2=|T_2|/n$, and $$W(C)=Cr\{f+f^2(k-1)^3L^2/m\}.$$ Choose natural numbers $n_W,n_P,D_p,T_\theta,s_\theta$, a real number $P_\theta$, and real constants $A_\theta,e_\theta,c_\theta,B_\theta,c_o,H_\theta,B'_\theta$. Require $$A_\theta\ge1,\quad e_\theta\ge12,\quad c_\theta\ge1,\quad B_\theta\ge0,\quad H_\theta\ge1,\quad B'_\theta\ge1,$$ $$P_\theta=A_\theta(frL)^{e_\theta},\quad D_p=f\binom r2,\quad n_P=8fr+4,\quad T_\theta=\lceil x^{c_o}\rceil_+,\quad r+t=n_P+T_\theta n_W.$$ The following are all the precision and size requirements: $$P_\theta,D_p,T_\theta\le x^{C_t},\quad W(C_W)\le n_W<W(C_W)+8,\quad8\mid n_W,$$ $$(2fm)^4n_W\le P_\theta,\quad n_W\le P_\theta,\quad fr(r+1)\le n_W,\quad(k-1)f+2r\le n_W,\quad n_P\le n_W,$$ $$\frac{P_\theta^4D_p^3kf x^{c_\theta}}{m\delta_2}\le T_\theta,\qquad T_\theta P_\theta x^{B_\theta}\le b,$$ $$(D_p+2)n_W+2r\le T_\theta,\quad40(D_p+2)\le T_\theta,\quad11D_p^2\le T_\theta,\quad r+4\cdot5^4r(D_p+1)\le T_\theta,$$ $$T_\theta P_\theta\le b^{1/2},\quad P_\theta^3T_\theta^2x^{B_\theta}\le b,\quad P_\theta^3T_\theta^2\le b^{1/2},\quad D_pk/m\le T_\theta,$$ $$T_\theta^2\le\Delta,\quad(T_\theta+D_p+2)(T_\theta+D_p+2+2N)\le\Delta,$$ $$4T_\theta^2+2t\le h_0,\quad P_\theta D_pfm^2NT_\theta\le h_0,\quad P_\theta(fmk)^3k/m\le h_0,$$ $$H_\theta T_\theta Nf^2m^2kD_pP_\theta\le h_0,$$ $$T_\theta D_p^2\log b\,x^{B_\theta}\le b,\quad T_\theta D_p^2\log b\le b^{1/2},\quad B'_\theta rmkP_\theta^2D_p^3\le b,$$ $$s_\theta\text{ odd},\qquad r+5<s_\theta\le r+7.$$ Here $C_t,C_W$ are the constants in ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)), $S=4k\Delta$, and $\lceil y\rceil_+=\max(0,\lceil y\rceil)$.
