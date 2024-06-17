import "process.arc"
// Comment

namespace NexovaBM.types { 
    Type Computer {
        List<String> Test
        List<Processes.Application> ATest
        String Name
        Number CPU
        Number Storage
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
        Name = "Windows"
        Status = E1.Test
               
        Release = {
            Major = 10
            Minor = 0
            Patch = 16299
            test = {
                test = 134
            }
        }
    }

    Instance Word of Application {
        Name = "Word"
    }

    Instance YourLaptop of Computer {
        Name = ["Windows", "linux"]
        Test = Word
        Release = {
            Major = 10
            Minor = 0
            Patch = 16299
            test = {
                test = 134
            }
        }
    }
}

