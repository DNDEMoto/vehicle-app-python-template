# Dev container environment with integrated Lingua Franca and Velocitas.

## Reference
[lf\-lang/lingua\-franca](https://github.com/lf-lang/lingua-franca)

[eclipse\-velocitas\-python\-template](https://github.com/eclipse-velocitas/vehicle-app-python-template)

## Change point

* .devcontainer/lf-scripts
* .devcontainer/devcontainer.json
* .devcontainer/Dockerfile
* .devcontainer/scripts/onCreateCommand.sh (only L30)

## Sample
Simple sample to access VSS data provided by Velocitas

* app/src/lf_velocitas.lf
* app/src/speed_app.py

### Build and Run

1. Execute the following command to generate the LF executable: `lfc app/src/lf_velocitas.lf`

1. Press F1 key and select "Tasks:Run Task", and select "Local Runtime - Up" to start the velocitas local runtime including can data stub.
1. Press F1 key and select "Tasks:Run Task", and select "Local Runtime - Run LF-Velocitas App"


