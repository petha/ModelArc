
# Model Arc Language

Model Arc is a domain-specific language for modeling business processes, applications, and infrastructure. It supports defining types, instances, enumerations, and transformations, providing a structured approach to represent complex systems.


**Note:** The language is currently in development and not ready for **any** use. The parser is partially working and currently builds an incomplete AST.

Still to do:
- importing of files
- Better AST
- Symbol tables and lookups 
- Type checking
- Transformation engine 
- Standard library of language constructs and transformation
- Backends for various compile targets


The idea is that the language can be used to:
- Simulate attack paths
- Instantiate testing infrastucture
- Security analysis and requirement engineering
- Render various projections like BPMN, Archimate, and other graphical notations
- Process simulation using virtualized or containerized representation of architecture.


## Features

- **Type Definitions**: Define complex types including nested structures and lists.
- **Instance Definitions**: Create instances of types with specific values.
- **Enum Definitions**: Define enumerations for sets of named constants.
- **Transformations**: Map types to other types, including enum transformations.
- **Imports**: Modularize your models by importing other files.
- **Namespaces**: Organize definitions logically to prevent name clashes.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/petha/ModelArc.git
    cd ModelArc
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Defining a Model

Create a `.arc` file with your model definitions. Here's an example:

```arc
import "common_types.arc"

namespace Company {
    // Define enums
    Enum Status {
        Ongoing,
        Closed,
        Completed
    }

    // Definition of Task
    Type Task {
        String name
        Number duration
        Status status
        List<Action> actions
    }

    Type Action {
        String command
    }

    // Definition of Device
    Type Device {
        String name     
    }

    Type VirtualMachine {
        String Name
        Number vCPU
        Number Memory
        String qcowImage
    }

    Type DockerContainer {
        String name
        String image

    }

    Type Computer extends Device {
        Number Storage
         os {
        
            String name
            String CPE
        
            release {
                Number major
                Number minor
                Number patch
            }
        }
    } 

    Transformation DockerTransform Computer -> DockerContainer {
        name -> name
        os.name -> image 
    }

    Instance MyComputer of Computer {
        name = "Vindalo 123"
        os = {
            name = "MultiHard Doors"
            CPE = "1234"
            release = {
                major = 10
                minor = 0
                patch = 1699
            }
        }
    }
}

```

## Usage 
Idea is that there will be several backends to output for instance
- Terraform definition of architecture 
- Ansible scripts for executions of processes
- BPMN representation of processes 
- Archimate XML for the various business architecture layers 

Currently the only output is a dump of the AST to the terminal

```bash
python main.py example/main.arc   
```

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Summary

- **Installation**: Provides steps to set up the project.
- **Usage**: Explains how to define models and parse them.
- **Features**: Lists the key features of the language.
- **Example**: Includes an example `.arc` file and how to parse it.
- **Contributing and License**: Basic contributing guidelines and license information.


