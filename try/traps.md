# Noticing abstraction traps

Programmers, data scientists and developers often have a deep understanding of the value of abstraction, and the complexity in drawing proper abstraction boundaries.

> Any problem in computer science can be solved with another layer of indirection. But that usually will create another problem.

Even naming things is hard!  And this is even harder in fairness work, but there are some helpful "abstraction traps" you can watch for when writing code or designing systems.

## a. Framing trap

When measuring performance, developers sometimes focus in too much on microbenchmarks that don't really reflect real-world performance.  The same thing can happen in fairness work.  If you're investigating the fairness of a classification system, make sure to consider that humans often don't exactly follow the recommendations of ML decisions systems.

Just like it can help ML systems to model the desired outcome end-to-end, it can help fairness work to understand the real deployment context for the system.  Adding 

> Failure to model the entire system over which a socialcriterion, such as fairness, will be enforced

## b. Portability trap
...
> Failure to understand how repurposing algorithmic solu-tions designed for one social context may be misleading,inaccurate, or otherwise do harm when applied to adifferent context

## c. Formalism trap
...
> Failure to account for the full meaning of social conceptssuch as fairness, which can be procedural, contextual,and contestable, and cannot be resolved through math-ematical formalisms

## d. Ripple Effect Trap
Debugging distributed systems is challenging, and observability and monitoring are critical parts of being able to understand and maintain such complex systems.  Changing one service may have impacts on another service that are difficult to understand.  This is even more challenging in ML systems, where shifts in data distributions can lead to large unexpected changes in behavior.

Working in fairness is similar; it is often very difficult to understand and predict how adding a new system into an existing team will change things, and how people will interpret ML systems and change their behavior in response.  Building open communication channels and ways to get continuous feedback is important in fairness work just as it is in distributed systems.

> Failure to understand how the insertion of technology into an existing social system changes the behaviors and embedded values of the pre-existing system

## e. Solutionism Trap
If you have a hammer, everything looks like a nail.

> Failure to recognize the possibility that the best solutionto a problem may not involve technology


???
https://xkcd.com/435/
