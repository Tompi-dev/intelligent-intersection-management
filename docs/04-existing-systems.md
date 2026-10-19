# Existing system comparison

Four relevant platforms are compared on eight shared criteria. These are research or engineering alternatives for building and evaluating signal-control systems, not four interchangeable roadside controllers. The proposed system adds a defined camera-to-demand-to-evaluation workflow; it is not claimed to replace mature commercial products. Entries are based on primary project or vendor material [S13 to S16]; an unconfirmed feature is not treated as absent.

| Criterion | SUMO S13 | CityFlow S14 | PTV Vissim S15 | Aimsun Next S16 |
|---|---|---|---|---|
| Primary use | Multimodal traffic research | City-scale traffic research | Microscopic traffic engineering | Transport modelling at multiple scales |
| Access model | Open-source project | Open-source project | Commercial; verify access | Commercial; verify edition |
| External control | TraCI | Python engine interface | Verify available API and edition | Python or C++ API; verify licence |
| Signal experiments | Documented traffic-light control | Signal-control research | Product-supported modelling; verify workflow | Product-supported modelling; verify workflow |
| Camera CV pipeline included in reviewed material | Not established | Not established | Not established | Not established |
| Suitability for one-junction baseline | Direct research fit | Feasible; larger-scale focus | Feasible if available | Feasible if available |
| Team reproducibility | Freeze open config and version | Freeze open config and version | Requires matching access and configuration | Requires matching access and configuration |
| Key project dependency | Geometry and TraCI integration | Engine build and scenario format | Licence and integration verification | Licence and integration verification |

SUMO is the proposed evaluation environment because its documented external-control interface fits the limited junction experiment. CityFlow is a credible research alternative. Commercial platforms may offer useful modelling workflows but cannot be assumed available to all team members. No price, accuracy ranking, or unsupported absence of functionality is asserted.

The project gap is an openly inspectable integration and evaluation study for the chosen scope, with traceable estimation error and controller decisions. Claims of novelty should concern the implemented integration and evaluation question, rather than the invention of object detection or adaptive signal control.
