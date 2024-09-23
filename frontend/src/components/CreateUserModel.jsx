import { Button, 
         Flex, 
         FormControl, 
         FormLabel, 
         Input, 
         Modal, 
         ModalBody, 
         ModalCloseButton, 
         ModalContent, 
         ModalFooter, 
         ModalHeader, 
         ModalOverlay, 
         Radio, 
         RadioGroup, 
         Textarea, 
         useDisclosure } from '@chakra-ui/react'
import React from 'react'
import { BiAddToQueue } from "react-icons/bi"

const CreateUserModel = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()
  return (
    <>
      <Button onClick={onOpen}>
        <BiAddToQueue size={20} />
      </Button>

      <Modal
        isOpen={isOpen}
        onClose={onClose}
      >
        <ModalOverlay />
        <ModalContent>
            <ModalHeader>Add new Staff</ModalHeader>
        <ModalCloseButton />
        

        <ModalBody pb={6}>
            <Flex alignItems={"center"} gap={4}>
                {/* left */}
                <FormControl>
                    <FormLabel>Full Name</FormLabel>
                    <Input placeholder="Name" />
                </FormControl>

                 {/* right */}
                 <FormControl>
                    <FormLabel>Role</FormLabel>
                    <Input placeholder="Position" />
                </FormControl>
            </Flex>

            <FormControl>
                <FormLabel>Description</FormLabel>
                <Textarea 
                    placeholder="I am a software Engineer woho loves to code and solve problem" 
                    resize={"none"}
                    overflowY={"hidden"}
                />
            </FormControl>

            <RadioGroup defaultValue="Male" nt={4}>
                <Flex gap={5}>
                    <Radio value='male'>Male</Radio>
                    <Radio value='female'>Female</Radio>
                </Flex>
            </RadioGroup>
        </ModalBody>

        <ModalFooter>
            <Button colorScheme='blue' mr={3}>
                Add
            </Button>
            <Button onClick={onClose}>Cancel</Button>
        </ModalFooter>

        </ModalContent>
      </Modal>

    </>
  )
}

export default CreateUserModel
