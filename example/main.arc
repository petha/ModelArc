import "process.arc"
// Comment

namespace NexovaBM.types { 
    Type Apa {
        String Name
        Number Age
    }

    Type Computer extends Apa {
        List<String> Test
        E1 Status
        List<Processes.Application> ATest
        Processes.Application OS
        String Name
        Number CPU
        Number Storage
        Vendor { 
            String Name
            String Address
        }
    }

    Type Application {
        String Name
        Release {
            Number value
            Nested {
                Number value
                Number test
            }
            
        }
    }
    
    Enum Status { 
        Ongoing,
        Closed,
        Completed
    }

    Enum E1 { 
        Test,
        Closed
    }

    Type Laptop extends Computer {
    
        String Name
    
        List<Application> Test

        Release {
            Number Major
            Number Minor
            Number Patch
            
            Release {
                Number Major
                Number Minor
                Number Patch
            }
        }
    }

    Transformation T1 Computer -> Application {
         "Computer Device" ->  name
    }

    Transformation T2 Status -> E1 {
        Ongoing -> Test
        Closed -> Closed
        Completed -> Completed
    }

    Transformation T3 Laptop -> Computer {
        vCPU -> CPU
        mem -> Memory using LaptopTrans
    }

    Instance MyLaptop of Computer {
        Age = 134
        CPU = 4
        Storage = 512
        OS = Word
        Status = E1.Closed
        Name = "MyLaptop"
        Test = ["Windowsf", "linux"]
        ATest = [Word]
        Vendor = {
            Name = "Dell"
            Address = "Bangalore"
        }
    }

    Instance Word of Application {
        Name = "Word"
        Release = {
            value= 12
            Nested = {
                value = 12
                test = 12
            }
            
        }
    }
}

