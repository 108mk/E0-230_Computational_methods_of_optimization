# E0-230_Computational_methods_of_optimization
This is my personal repository for E0: 230:Computational Method of Optimization by Prof. Chianjib Bhattacharya at IISc Bengaluru. It is a course on mathematical optimization offered by the computer science department. You can find my codes and assignment solution along with class notes. Feel free to fork and use. Don't hesitate to report mistakes if you find them in the documents.

:accessibility: Highlights of crucial optimization algorithms and tactics along with their real-world applications:

## Books: 
> R. Fletcher:   Practical Methods of Optimization (Volume 1 &2)

> David G. Luenberger, Yinyu Ye:   Linear and Nonlinear Programming

> Yu. Nesterov:   Introductory Lectures on Convex Programming

## Standard Optimization Problem Template
Objective function $f:\mathbb{R}^d \to \mathbb{R}$

 Constrain: $S\subset \mathbb{R}^d$

 Find $x^{\ast}=argmin_{x\subset S}\ f(x)$
 and $f(x^{\ast})$

### Standard iterative algorithm:

 pick $x\in S$

 $\textbf{while}\ x$  is not optimal solution $\textbf{do}:$
 
 Pick another $x\in S$ such that $f(x)$ decreases;
 
 $\textbf{end}$

 return $(x,\ f(x))$

## Part-I: Mathematical foundation of optimization theory

 $\bullet$ Mathematical Analysis: $[\delta - \epsilon]$ definition of Limit
 $\bullet$ Lipshitz Continuity
 
 $\bullet$ Asymptotic notations: $\mathcal{O}(f(x)),\mathcal{\Omega}(f(x))\ and\ \mathcal{o}(f(x)) $
 $\bullet$ Metric Space: Open and Compact sets

 $\bullet$ Multivariate Calculus and Tylor Series Analysis

 $\bullet$ Weistrass theorem: the existence of minima and maxima of a function
 
 $\bullet$ Gradient and Hessian of a function: Sufficient condition for the existence of local minima
 
 $\bullet$ Analysis of special matrices: Positive definite (PD), negative definite(ND) and positive semi-definite (PSD) matrices


## Part-II: Convex Function and its Optimization 

⭐ $\bullet$ Convex function and existence of global minima

 Quadratic form and closed form solution:

 $f(x)=x^TQx-d^Tx \implies \nabla f(x) = Qx-d\ and\ H(f(x))=Q$

 $\implies x^{\ast} = Q^{-1}d$

 Computational complexity: $\mathcal{O}(n^3)$ via Gauss Elimination [Hence, practically useless for large matrices]

 Descent-based algorithm for approximately searching the minima:
 
Exact line search: Kantarovich inequality
 
Bounded Hessian Quadratic functions: $AI-H_f(x)\ and\ aI-H_f(x)$ are hessian $\forall x$

Ineaxct line search: Goldstein and Wolfe condition

## Part-III: First-order methods for optimizations
⭐ Coordinate descent algorithm
 Criteria for convergence of coordinate descent algorithms

⭐ Conjugate descent algorithm:

> Algorithm for Q-conjugate
>> Determining Q-conjugate vectors
>>
>> Expanding subspace theorem
>> 
> Faster convergence for the structured eigenvalue of the Q matrix
>>
>> Case of distinct eigenvalue of Q.
>>
>> Polynomial method for conjugate descent
>>
>> The case of Clustered eigenvalue
>>
## Part-IV: Second-order methods for optimizations
⭐ Newton's Methods
> Region of positive definite Hessian
>
> Newton's region and convergence criteria
>
⭐ Quasi-Newton Methods
> Rank-1 update technique
>
> Rank-2 update technique
>
> BFGS technique
>
> Broyden Family

## Part-V: Constrained Optimization
$x^{*}=argmin_{x\in C}(f(x))\ where\ C \in \mathbb{R}^d$ over constrained set C.

> Projection into a convex set
 
> Separating Hyper space theorem

> Optimization under Inequality constraints:
> 
>> Farkas Lemma
>>
>> KKT condition as a necessary condition for minima

⭐ Projected Gradient Descent

⭐ Active set method

## Video Lecture link (2021 offering): 

https://drive.google.com/drive/folders/1tngztngZpOC1VFYTLgwvLnJRypRuvHXn?usp=sharing

## Website (2019 offereing):
https://cmo2019.github.io/cmo2019/

