import "./ProfileModal.css";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import emptyUserImage from "../../assets/images/empty-user-img.png";
import { User } from "../../interfaces/interfaces";

interface ProfileModalProps {
  visible?: boolean;
  setIsVisible: (active: boolean) => void;
  user: User | null
}

function ProfileModal({ visible = false, setIsVisible, user }: ProfileModalProps) {
  return (
    <Modal className="profile-modal" show={visible} centered>
      <Modal.Header className="justify-content-center">
        <h2>Perfil</h2>
      </Modal.Header>
      <Modal.Body>
        <div className="profile-image-container">
          <img
            src={emptyUserImage}
            alt="Empty User Image"
            className="profile-image"
          />
        </div>

        <div className="profile-content-container">
          <p><b>Id: </b> {user?.id} </p>
          <p><b>Usuário: </b> {user?.username} </p>
          <p><b>Email: </b> {user?.email} </p>
          <p><b>É admin: </b> {user?.is_staff ? "Sim" : "Não"} </p>
        </div>
      </Modal.Body>

      <Modal.Footer>
        <Button variant="secondary" onClick={(e) => setIsVisible(false)}>
          Fechar
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default ProfileModal;
