---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/HookProducts/Compl3Record.lean",
  "declarations": [
    "Formalism.MainNotions.DIV.HookProducts.RBCompl3.compl3_record",
    "Formalism.MainNotions.DIV.HookProducts.RBCompl3.log_M_le",
    "Formalism.MainNotions.DIV.HookProducts.RBCompl3.rbCompl3"
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

## Uniform variation of the adjusted source heights

[Theorem ARAK.0175](https://andrewodesky.com/rh/lean/Formalism.MainNotions.DIV.HookProducts.RBCompl3.rbCompl3/)

Use the full arithmetic-family datum of ([Integral maps with height and target bounds](https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkDIV_at/)), including its parameter-choice and size conditions, starting scale $x_1$, and fixed exponent $\varepsilon>0$. Let $h_u$ be its explicitly specified source height bounds, not arbitrary map-height bounds, and put $A_0=\sum_{t\in T}a_t$, $L=x^\varepsilon$, $b=e^L$, and $B_0=fmbL$. Then, for every $x\ge x_1+1$, every family member at $x$, and every $u,u'$, $$\left|(h_u+A_0\log T_u)-(h_{u'}+A_0\log T_{u'})\right|\le\left(20+\frac6\varepsilon\right)\{|T|a\mathcal L+mB_0\}.$$ The same bound holds at an individual arithmetic datum satisfying its full parameter-choice and size conditions, with its specified height formula and with any real value of the coefficient $C_{\rm sz}$ occurring in that formula.

## Numerical variation bound from adjusted height differences

[Theorem ARAK.1740](https://andrewodesky.com/rh/lean/Formalism.MainNotions.DIV.HookProducts.RBCompl3.log_M_le/)

For every scale $x>1$, $0<\varepsilon<1/52$, $J\ge1$, put $L=x^\varepsilon$ and $b=e^L$. Then $$\log(6x^6b)\le5+\frac{6L}{\varepsilon}+L.$$

Use the arithmetic field, group, rank, coefficient and weight data of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)), including its Galois action, prescribed subsets of embeddings and prime choices, and assume its parameter-choice hypothesis and the size conditions below. In particular $x>1$, $0<\varepsilon<1/52$, $J\ge1$, $L=x^\varepsilon$, $b=e^L$, $a=xb$, and $B_0=fmbL$. Write $\mathcal U$ for its finite nonempty set of source indices, $T_u$ for its prescribed source primes, and put $$A_0=\sum_{v\in T}a_v,\qquad \mathcal L=\log(a\operatorname{rd}_E),\qquad \omega=\gamma+\log(2\pi/\operatorname{rd}_E)-\Re\frac{L'}L(1,\chi_d),$$ where $\gamma$ is Euler's constant and $\operatorname{rd}_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]}$. For every real $C_{\rm sz}$, define the explicit heights $h_u$ by the formula below, using the positive period factors of the arithmetic moduli data. Then, for every $u,u'\in\mathcal U$, $$\left|(h_u+A_0\log T_u)-(h_{u'}+A_0\log T_{u'})\right| \le\left(20+\frac6\varepsilon\right)\left\{|T|\,xb\log(xb\operatorname{rd}_E)+mB_0\right\}.$$ The first term on the right is fixed by the arithmetic data.
