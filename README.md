# Lingua Franca and Velocitas.

## Reference
[lf\-lang/lingua\-franca](https://github.com/lf-lang/lingua-franca)

[eclipse\-velocitas\-python\-template](https://github.com/eclipse-velocitas/vehicle-app-python-template)

## What is this?
Lingua Franca runtime are integrated based on velocitas python app template.

The changes from velocitas python app template are as follows

* .devcontainer/lf-scripts
* .devcontainer/devcontainer.json
* .devcontainer/Dockerfile
* .devcontainer/scripts/onCreateCommand.sh (only L30)

## LF-Velocitas Bridge sample application

Simple sample to access VSS data provided by Velocitas

## Polling sample

* app/src/lf_velocitas_polling/lf_velocitas_e.lf
* app/src/lf_velocitas_polling/speed_app.py

## Event trigger sample

* app/src/lf_velocitas_event/lf_velocitas_p.lf

### Build and Run

1. Execute the following command to generate the LF executable: `lfc app/src/lf_velocitas_event/lf_velocitas_e.lf`

1. Press F1 key and select "Tasks:Run Task", and select "Local Runtime - Up" to start the velocitas local runtime including can data stub.
1. Press F1 key and select "Tasks:Run Task", and select "Local Runtime - Run LF-Velocitas Event App"
